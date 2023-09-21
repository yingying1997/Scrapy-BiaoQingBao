# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy # 导入 Scrapy 库，用于构建爬虫


class BiaoqingbaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()
    # 图片标题
    img_title = scrapy.Field()
    pass
