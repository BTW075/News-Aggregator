import requests
from bs4 import BeautifulSoup

class DataCollector: 
    def __init__(self, url):
        self.url = url        

# this method retreives the xml data as it is from the RSS feed url.
    def get_data(self, url):
        response = requests.get(url)
        xmlContent = BeautifulSoup(response.content, 'xml')
        return xmlContent
    
    def get_item(self, xmlContent):
        items = xmlContent.find_all('item')
        return items       
         
    
    def get_titleList(self, items):
        titleList = []
        # return titles
        for item in items:
            title = item.find('title').text.strip()
            titleList.append(title)       
        return titleList
    
    
#Now to get the description of the news
    def get_descriptionList(self, items):        
        descriptionList = []
        
        for item in items:
             description = BeautifulSoup(item.find('description').text.strip(), 'html.parser').get_text()
             descriptionList.append(description)        
        return descriptionList
    
# now to retreive the link to read more about the news
    def get_linkList(self, items):        
        linkList = []        
        for item in items:
             link = item.find('link').text.strip()
             linkList.append(link)        
        return linkList

# TO retreive the list if all publish dates of the news
    def get_DateList(self, items):        
        DateList = []        
        for item in items:
             pub_date = item.find('pubDate').text.strip()
             DateList.append(pub_date)
        return DateList



if __name__ == '__main__':
    test = DataCollector('https://timesofindia.indiatimes.com/rssfeeds/1898055.cms')    
    # print(test.get_titleList(test.get_item(test.get_data(test.url))))
    # print(test.get_descriptionList(test.get_item(test.get_data(test.url))))
    # print(test.get_linkList(test.get_item(test.get_data(test.url))))
    # print(test.get_DateList(test.get_item(test.get_data(test.url))))
    print()
