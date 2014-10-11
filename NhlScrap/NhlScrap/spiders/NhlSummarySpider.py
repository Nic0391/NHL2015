import scrapy
import sys
from scrapy.http import Request
from NhlScrap.parsers.SummaryParser import parseSummary

class NhlPBPSpider(scrapy.Spider):
    name = "NhlSummarySpider"
    allowed_domains = ["nhl.com"]
    siteRange = range(20000, 20017);

    def start_requests(self):
        for i in self.siteRange:
            yield Request('http://www.nhl.com/scores/htmlreports/20142015/ES0%d.HTM' % i,
                callback = self.parse)

    def parse(self, response):
    	for table in response.xpath('//html/body/table/tr[8]/td/table'):
            lines = table.xpath('./tr')
            item = parseSummary(lines)
        item['url'] = response.url
        yield item