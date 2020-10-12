# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class GetFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Alice', 'Bob', 'Charles']
        quests = ['to seek the grail', 'to learn Python', 'to scrape the web']
        return [FormRequest(
            'http://pythonscraping.com/linkedin/formAction2.php',
            formdata={'name': name, 'quest': quest, 'color': 'blue'},
            callback=self.parse)  for name in names for quest in quests]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
