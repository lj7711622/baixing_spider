# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BaixingSpiderPipeline(object):

	def open_spider(self, spider):
		self.file = open('xu_hui.txt', 'w',encoding='utf-8')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		line = json.dumps(dict(item),indent=1,ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	# collection_name = 'zhengzu'

	# def __init__(self, mongo_uri, mongo_db):
	# 	self.mongo_uri = mongo_uri
	# 	self.mongo_db = mongo_db

	# @classmethod
	# def from_crawler(cls, crawler):
	# 	return cls(
	# 		mongo_uri=crawler.settings.get('MONGO_URI'),
	# 		mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
	# 	)

	# def open_spider(self, spider):
	# 	self.client = pymongo.MongoClient(self.mongo_uri)
	# 	self.db = self.client[self.mongo_db]

	# def close_spider(self, spider):
	# 	self.client.close()

	# def process_item(self, item, spider):
	# 	self.db[self.collection_name].insert_one(dict(item))
	# 	return item
