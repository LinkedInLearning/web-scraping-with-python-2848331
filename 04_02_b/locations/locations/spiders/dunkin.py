# -*- coding: utf-8 -*-
import scrapy

class DunkinSpider(scrapy.Spider):
    name = 'dunkin'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.dunkindonuts.com/en/locations?location=02155']

    def parse(self, response):
        return { 'addresses': response.xpath('//div[@class="store-item__address--line1"]/text()').getall() }
