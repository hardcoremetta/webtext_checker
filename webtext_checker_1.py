from scrapy import Spider, crawler, http
ENVIRONMENT = "IMP"
URL = "http://smartreward-imp.tbs.aon.com/Benefits-Overview-(1)"
USERNAME = "KrzysTEST"
PASSWORD = "P@ssword123"
class WebsiteAccess(Spider):
    name = ENVIRONMENT
    allowed_domains = ['imp.tbs.aon.com', 'tbs.aon.com',]
    start_urls = [URL]
    
    # def __init__(self, name, url, username, password):
    #     super().__init__(name)
    #     self.url = url
    #     self.username = username
    #     self.password = password
    def login(self):
        return [
            http.FormRequest(
                "https://smartreward-imp.tbs.aon.com/logon.aspx?ReturnUrl=%2fBenefits-Overview-(1)", 
                formdata=
                    {
                        "username": USERNAME,
                        "password": PASSWORD,
                    },
                callback=self.parse,
            )
        ]
    def parse(self, response):
        print(response.body)
        print("______________________________________________________________________________________")
if __name__ == "__main__":
    process = crawler.CrawlerProcess()
    process.crawl(WebsiteAccess)
    process.start()