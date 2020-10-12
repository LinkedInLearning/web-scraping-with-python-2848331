# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle

def generate_start_urls():
        years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        return ['https://www.cnn.com/sitemaps/article-{}-{}.xml'.format(year, month) for year in years for month in months]

class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = generate_start_urls()
    
    def parse(self, response):
        return {'url': response.url, 'count': response.text.count('<url>')}

