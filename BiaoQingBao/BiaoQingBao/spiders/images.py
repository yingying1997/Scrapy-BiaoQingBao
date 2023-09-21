import scrapy # 导入 Scrapy 库，用于构建爬虫
import re # 导入 re 模块，用于进行正则表达式匹配
from BiaoQingBao.items import BiaoqingbaoItem # 导入自定义的 Item 类，用于存储爬取的数据

class SpiderSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'images'
    # 允许爬取的域名
    # allowed_domains = ['fabiaoqing.com']
    # 链接 url
    base_url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
    # 页码
    page = 1
    # 起始 url
    start_urls = [base_url.format(page)]

    def parse(self, response):
        # 解析数据，找所有的 img 标签
        images = response.xpath('//img[@class="ui image lazy"]')
        # 遍历获取每一个 img 标签，解析里面的图片 url 以及标题
        for img in images:
            # 创建一个 MyScrapyItem 实例，用于存储爬取的数据
            item = BiaoqingbaoItem()
            # 图片 url
            item['img_url'] = img.xpath('@data-original').get()
            # 标题
            title = img.xpath('@title').get()
            # 正则表达式替换标题特殊字符
            item['img_title'] = re.sub(r'[?/\\<>*:(), ]', '', title)
            # 返回 item，将其传递给引擎
            yield item

        # 进行翻页处理
        if self.page <= 10:
            self.page += 1
            # 获取数据
            yield scrapy.Request(self.base_url.format(self.page), callback=self.parse)