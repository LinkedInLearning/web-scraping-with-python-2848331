# -*- coding: utf-8 -*-
from datetime import datetime

class NewsScraperPipeline:
    def process_item(self, item, spider):
        item.date = datetime.strptime(item.date.split('T')[0], '%Y-%B-%D')
        item.author = item.author.replace(', CNN', '')
        item.text = [text.strip() for text in item.text]
        return item
