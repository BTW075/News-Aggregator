import requests
from bs4 import BeautifulSoup

class DataCollector: 
    def __init__(self, url, CatagoryKeyWord, sourceLink):
        self.url = url
        self.CatagoryKeyWord
        self. sourceLink

# this method retreives the xml data as it is from the RSS feed url.
    def get_data(self, url):
        response = requests.get(url)
        xmlContent = BeautifulSoup(response.content, 'xml')
        return xmlContent
    
    def get_titleList(self, xmlContent):
        titles = xmlContent.find_all('title')
        titleList = []
        #return titles
        for title in titles:
             t = title.text.strip()
             titleList.append(t)
        CatagoryKeyWord = titleList.pop(0) # Removes the first element from list and stores in variable
        return titleList
    
    
#Now to get the description of the news
    def get_descriptionList(self, xmlContent):
        description = xmlContent.find_all('description')
        descriptionList = []
        
        for des in description:
             d = des.text.strip()
             descriptionList.append(d)
        del descriptionList[0] #delete the first description
        return descriptionList
    
# now to retreive the link to read more about the news
    def get_linkList(self, xmlContent):
        links = xmlContent.find_all('link')
        linkList = []
        
        for link in links:
             l = link.text.strip()
             linkList.append(l)
        sourceLink = linkList.pop(0) # delete the first link and save it in variable.
        return linkList

# TO retreive the list if all publish dates of the news
def get_DateList(self, xmlContent):
        pub_dates = xmlContent.find_all('pubDate')
        DateList = []
        
        for dates in pub_dates:
             p = dates.text.strip()
             DateList.append(l)
        return DateList



if __name__ == '__main__':
    test = DataCollector('https://timesofindia.indiatimes.com/rssfeeds/1898055.cms')
    test.get_data(test.url)
    #print(test.get_titleList(test.get_data(test.url)))
    # print(test.get_descriptionList(test.get_data(test.url)))
    print(test.get_linkList(test.get_data(test.url)))
    print()
