# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from datetime import datetime

class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['lastUPdated'] or not article['url'] or not article['title']:
            raise DropItem('Missing something!')
        return article


class CleanDatePipeline:
    def process_item(self, article, spider):
        article['lastUpdated'].replace('This page was last edited on', '').strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M')
        return article
