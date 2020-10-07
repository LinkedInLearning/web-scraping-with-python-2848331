# -*- coding: utf-8 -*-
import json
from news_scraper.items import NewsArticle
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class YahooSpider(CrawlSpider):
    name = 'yahoo'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']
    rules = [Rule(LinkExtractor(allow=r'\/[a-zA-Z\-]+-[0-9]+.html'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'Yahoo News'

        
        jsonData = json.loads(response.xpath('//article[@role="article"]/script[@type="application/ld+json"]/text()').get())

        article['title'] = jsonData['headline']
        article['description'] = jsonData['description']
        article['date'] = jsonData['datePublished']
        article['author'] = jsonData['author']['name']
        article['text'] = response.xpath('//div[@class="caas-body"]/p/text()').getall()
        return article
