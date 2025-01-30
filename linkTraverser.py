from dataCollector import DataCollector
from sql import SQLQueries

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
            items = self.get_item(xmlContent)
            titles = self.get_titleList(items)
            descriptions = self.get_descriptionList(items)
            news_links = self.get_linkList(items)
            pub_date = self.get_DateList(items)

            SQLQueries.store_feed(titles, descriptions, source, category, news_links, pub_date)

            self.show(titles, descriptions, news_links,pub_date)

    def show(self, titles, descriptions, news_links, pub_date) :
        print(titles,"\n")
        print(descriptions,"\n")
        print(news_links,"\n")
        print(pub_date,"\n")            

if __name__ == "__main__":
    link_traverser = LinkTraverser("business-RSS-Feeds.txt")
    link_traverser.traverse_links()
