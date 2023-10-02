from parsel import Selector
import  requests



class Newscraper:
    PLUS_URL = 'https://www.prnewswire.com'
    URL ="https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100"
    LINK_XPATH = '//div[@class="row newsCards"]/div/a/@href'
    TITLE_XPATH = '//div[@class="row newsCards"]/div/a/div[2]/h3/text()'


    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        titles = tree.xpath(self.TITLE_XPATH).extract()
        # for link in links:
        #     print(self.PLUS_URL + link)
        #     print(self.TITLE_XPATH)
        # for title in titles:
        #     print(title)
        return links[:5]

if __name__ == "__main__":
    scraper = Newscraper()
    scraper.parse_data()
