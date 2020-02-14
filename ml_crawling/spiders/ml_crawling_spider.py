import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider


from ml_crawling.items import MlCrawlingItem

class mlSpider(CrawlSpider):
    name='ml_crawling' #este es el nombre que se le da en la consola
    item_count=0 # conteo para el numero de items a tomar
    allowed_domain=['https://www.mercadolibre.com.mx/']
    start_urls=["https://listado.mercadolibre.com.mx/impresoras#D[A:impresoras]"]
    rules={
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//li[@class="pagination__next"]/a'))),
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//h2[@class="item__title list-view-item-title"]')),
        callback='parse_item',follow=False)
    }

    def parse_item(self,response):
        ml_item=MlCrawlingItem() #Instancia de la clase MlCrawlingItem en items.py
        #Importar los items de la Info. del producto
        ml_item['titulo']=response.xpath('normalize-space(//h1[@class="item-title__primary"]/text())').extract()
        ml_item['folio']=response.xpath('//span[@class="item-info__id-number"]/text()').extraxt()
        ml_item['precio']=response.xpath('//span[@class="price-tag"]/span[2]/text()').extract()
        ml_item['condicion_ventas']=response.xpath('normalize-space(//dl[@class="vip-title-info"]/div/text())').extract()
        ml_item['envio']=response.xpath('normalize-space(//p[@class="shipping-method-title shipping-text free-shipping"]/text())').extract()
        ml_item['ubicacion']=response.xpath('//p[@class="card-description text-light"]/strong/text()').extract()
        ml_item['opiniones_puntos']=response.xpath('//div[@class="card-section"]/span/text()').extract()
        #Info del vendedor
        ml_item['vendedor_url']=response.xpath("//*[starts-with(@class,'reputation-view-more')]/@href").extract()
        ml_item['tipo_vendedor']=response.xpath('/html/body/main/div/div[1]/div[2]/div[1]/section[2]/div[2]/p[1]').extract()
        ml_item['reputacion_puntos']=response.xpath('normalize-space(//*[@id="productInfo"]/div[5]/div[2]/p/text())').extract()
        ml_item['ventas_vendedor']=response.xpath('/html/body/main/div[2]/div[1]/div[2]/div[1]/section[2]/div[4]/dl/dd[1]/strong/text()').extract()

        self.item_count+=1

        if self.item_count>70:
            raise CloseSpider('item_exceeded')
        yield ml_item
