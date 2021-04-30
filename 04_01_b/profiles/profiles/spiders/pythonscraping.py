# -*- coding: utf-8 -*-
import scrapy


class PythonscrapingSpider(scrapy.Spider):
    name = 'pythonscraping'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']


    def parse(self, response):
        return { 'text': response.xpath('//body/text()').get() }
