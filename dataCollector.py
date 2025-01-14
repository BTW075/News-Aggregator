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
    
    def get_titleList(self, xmlContent):
        titles = xmlContent.find_all('title')
        titleList = []
        #return titles
        for title in titles:
             t = title.text.strip()
             titleList.append(t)
        return titleList
    
    #might not need this one
    # def get_title(self, titleList):
    #     for i in range(len(titleList)):
    #         each = titleList[i]
    #         yield each # will give each title one by one but well see later

#Now to get the description of the news
    def get_descriptionList(self, xmlContent):
        description = xmlContent.find_all('description')
        descriptionList = []
        
        for des in description:
             d = des.text.strip()
             descriptionList.append(d)
        return descriptionList
    
# now to retreive the link to read more about the news
    def get_linkList(self, xmlContent):
        links = xmlContent.find_all('link')
        linkList = []
        
        for link in links:
             l = link.text.strip()
             linkList.append(l)
        return linkList



if __name__ == '__main__':
    test = DataCollector('https://timesofindia.indiatimes.com/rssfeeds/1898055.cms')
    test.get_data(test.url)
    #print(test.get_titleList(test.get_data(test.url)))
    # print(test.get_descriptionList(test.get_data(test.url)))
    print(test.get_linkList(test.get_data(test.url)))
