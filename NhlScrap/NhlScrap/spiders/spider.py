import scrapy
import sys
from scrapy.http import Request
from NhlScrap.items import NhlItem	
from NhlScrap.parsers.PlayFieldsParser import parseFields

class NhlSpider(scrapy.Spider):
    name = "Nhl"
    allowed_domains = ["nhl.com"]
    siteRange = range(20000, 20017);

    def start_requests(self):
        for i in self.siteRange:
            yield Request('http://www.nhl.com/scores/htmlreports/20142015/PL0%d.HTM' % i,
                    callback = self.parse)

    def parse(self, response):
    	item = NhlItem()
    	item['url'] = response.url
    	item['plays'] = []
    	for line in response.xpath('//tr[contains(@class, "evenColor")]'):
    		fields = line.xpath('./td')
    		playItem = parseFields(fields)
    		item['plays'].append(dict(playItem))
    	yield item