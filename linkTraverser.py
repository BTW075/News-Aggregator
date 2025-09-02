from dataCollector import DataCollector
import SQlQuerries

## to inherit DataCollector 
class LinkTraverser(DataCollector) :
    def __init__(self, link_file) :
        self.link_file = link_file 
        self.links = self.read_links()

## to read the links file
    def read_links(self) : 
        with open(self.link_file, "r") as file :
            return [link.strip() for link in file.readlines()]

## to traverse each link from the link file and print relevant data
    def traverse_links(self):
        for link in self.links:
            try:
                category, source, feedLink = map(str.strip, link.split(","))
                super().__init__(feedLink)

                xmlContent = self.get_data(feedLink)
                items = self.get_item(xmlContent)

                if not items:
                    print(f"No articles found in feed: {feedLink}")
                    continue

                titles = self.get_titleList(items)
                descriptions = self.get_descriptionList(items)
                news_links = self.get_linkList(items)

                SQlQuerries.store_feed(titles, descriptions, news_links, category, source)

                self.show(titles, descriptions, news_links)
                print(f"Inserted {len(titles)} articles from {source} - {category}")

            except Exception as e:
                print(f"Error processing feed '{feedLink}' from {source}: {e}")

    def show(self, titles, descriptions, news_links) :
        print(titles,"\n")
        print(descriptions,"\n")
        print(news_links,"\n")            

if __name__ == "__main__":
    link_traverser = LinkTraverser("RSS-Feeds")
    link_traverser.traverse_links()
