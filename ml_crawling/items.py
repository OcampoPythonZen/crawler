# -*- coding: utf-8 -*-
# Define here the models for your scraped items
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class MlCrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Info. del producto
    titulo=scrapy.Field()
    folio=scrapy.Field()
    precio=scrapy.Field()
    condicion_ventas=scrapy.Field()
    envio=scrapy.Field()
    ubicacion=scrapy.Field()
    opiniones_puntos=scrapy.Field()
    #Info. de la tienda o vendedor
    vendedor_url=scrapy.Field()
    tipo_vendedor=scrapy.Field()
    reputacion_puntos=scrapy.Field()
    ventas_vendedor=scrapy.Field()
