import scrapy
import sys
from scrapy.http import Request
from NhlScrap.parsers.SummaryParser import parseSummary

class NhlPBPSpider(scrapy.Spider):
    name = "NhlSummarySpider"
    allowed_domains = ["nhl.com"]
    siteRange = range(20015, 20017);

    def start_requests(self):
        yield Request('http://www.nhl.com/scores/htmlreports/20142015/ES020015.HTM',
                callback = self.parse)

    def parse(self, response):
    	for table in response.xpath('//html/body/table/tr[8]/td/table'):
            lines = table.xpath('./tr')
            item = parseSummary(lines)
        item['url'] = response.url
        yield item