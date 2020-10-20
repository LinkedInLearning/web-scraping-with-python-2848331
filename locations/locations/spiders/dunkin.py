# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy_selenium import SeleniumRequest

def wait(driver):
    time.sleep(1)
    return True

class DunkinSpider(scrapy.Spider):
    name = 'dunkin'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.dunkindonuts.com/en/locations?location=02155']


    def make_requests_from_url(self, url):
        return SeleniumRequest(url=url, wait_time=10, wait_until=wait)

    def parse(self, response):
        return { 'addresses': response.xpath('//div[@class="store-item__address--line1"]/text()').getall() }
