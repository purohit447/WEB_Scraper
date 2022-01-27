# -*- coding: utf-8 -*-
import scrapy


class ContriesSpider(scrapy.Spider):
    name = 'contries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/population/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//ul/li/a/text()").getall()
        yield{
            'title' : title,
            'countries' : countries
        }
       

    
       