# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy # 导入 Scrapy 库，用于构建爬虫
from itemadapter import ItemAdapter # 导入 itemadapter 模块中的 ItemAdapter 类，用于简化和处理爬虫中的数据项
from scrapy.pipelines.images import ImagesPipeline # 导入 scrapy.pipelines.images 模块中的 ImagesPipeline 类，用于处理爬取的图片数据

# 定义 BiaoqingbaoPipeline 类，继承自 ImagesPipeline 类
class BiaoqingbaoPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    # 请求头
    head = {
        'Referer': 'https://fabiaoqing.com/'
    }
    # 专门下载图片的方法
    def get_media_requests(self, item, info):
        # 获取图片 url
        img_url = item['img_url']
        # 发起图片下载请求
        yield scrapy.Request(img_url, headers=self.head)

    # 重新给图片命名
    def file_path(self, request, response=None, info=None, *, item=None):
        # 名称
        img_name = item['img_title']
        # 指定保存文件夹
        return f'full/{img_name}.jpg'