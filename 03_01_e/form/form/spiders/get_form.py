# -*- coding: utf-8 -*-
import scrapy

def generate_start_urls():
    names = ['Alice', 'Bob', 'Charles']
    quests = ['to seek the grail', 'to learn Python', 'to scrape the web']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=blue'.format(name, quest.replace(' ', '%20')) for name in names for quest in quests]
    return quests 


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
