from dataCollector import DataCollector

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
    def traverse_links(self) :
        for link in self.links :
            # link = Business, Times of India, rss feed url
            seperateLinkItems = str.split(link,",")
            category = seperateLinkItems[0]
            source = seperateLinkItems[1]
            feedLink = seperateLinkItems[2]
            
            super().__init__(link)
            xmlContent = self.get_data(feedLink)
            titles = self.get_titleList(xmlContent)
            descriptions = self.get_descriptionList(xmlContent)
            news_links = self.get_linkList(xmlContent)

            SQLQueries.store_feed(titles, descriptions, news_links, category, source)

            self.show(titles, descriptions, news_links)

    def show(self, titles, descriptions, news_links) :
        print(titles,"\n")
        print(descriptions,"\n")
        print(news_links,"\n")            

if __name__ == "__main__":
    link_traverser = LinkTraverser("business-RSS-Feeds")
    link_traverser.traverse_links()
