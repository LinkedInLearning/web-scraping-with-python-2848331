# -*- coding: utf-8 -*-
import scrapy


class PythonscraperSpider(scrapy.Spider):
    name = 'pythonscraper'
    allowed_domains = ['pythonscraper.com']
    start_urls = ['http://pythonscraper.com/linkedin/cookies/profile.php']

    def parse(self, response):
        return { 'text': response.xpath('//body/text()').get() }
