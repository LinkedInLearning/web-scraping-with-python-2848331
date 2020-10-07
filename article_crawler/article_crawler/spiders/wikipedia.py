# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [
        Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)
    ]

    def parse_info(self, response):
        return {
            "title": response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()'),
            "url": response.url,
            "last_edited": response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        }
