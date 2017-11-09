# -*- coding: utf-8 -*-
import scrapy
from baixing_spider.items import BaixingSpiderItem
import time 
import re

class ZhengzuSpider(scrapy.Spider):
	name = "zhengzu"
	allowed_domains = ["shanghai.baixing.com"]
	start_urls = [
	    "http://shanghai.baixing.com/zhengzu/m7262/?grfy=1&%E4%BB%B7%E6%A0%BC%5B0%5D=1500&%E4%BB%B7%E6%A0%BC%5B1%5D=2500"
	]

	def parse(self, response):
		for sel in response.css('ul.list-ad-items > li.item-regular'):
			detail_url = sel.css('a.ad-title::attr(href)').extract()[0]
			title = sel.css('a.ad-title::text').extract_first()
			price = sel.css('span.highlight::text').extract_first()
			detail = sel.css('div.ad-item-detail::text')[0].extract()
			address = sel.css('div.ad-item-detail::text')[1].extract()
			publish_date = sel.css('div.ad-item-detail')[1].css('time::text').extract_first()
			time.sleep(1) # 暂停 1 秒  
			yield scrapy.Request(url = detail_url, meta = {"title":title, "price":price, "detail":detail, "address":address,"publish_date":publish_date}, callback=self.parse_item, dont_filter=True)

	def parse_item(self, response):
		item = BaixingSpiderItem()
		item['title'] = response.meta["title"]
		item['url'] = response.url
		item['price'] = response.meta["price"]
		item['mobile'] = response.css('div.infoPart > p > strong::text').extract()[0]
		item['detail'] = response.meta["detail"]
		item['address'] = response.meta["address"]
		item['publish_date'] = response.meta["publish_date"]
		item['lng'] = re.findall('lng = ([0-9\.]*)',response.body.decode('utf-8'))[0].strip()
		item['lat'] = re.findall('lat = ([0-9\.]*)',response.body.decode('utf-8'))[0].strip()
		yield item