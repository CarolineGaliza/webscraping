#Atividade de WebScrapping
#Alunas: Caroline Galiza e Marcela Carvalho
#Questão 02 - > Mercado Livre

#Comando de execução do projeto:   # scrapy runspider MLSpider.py -a produto="capinha de celular"

#Importando o scrapy
#Usando o recurso de abrir no browser para pegar as classes dos elementos
import scrapy
from scrapy.utils.response import open_in_browser

#Definindo a classe
class MLSpider(scrapy.Spider):
    #Nomeando a classe
    name = "mlspider"

    def __init__(self, produto="", **kwargs):
        self.start_urls = {"https://lista.mercadolivre.com.br/%s" % produto}
        super().__init__(**kwargs)

    #Captando o preço do produto
    def parse(self, response):
        nomes_produtos = response.css(".main-title::text").extract()
        preco_produtos = []

        for item in response.css(".item__price"):
            preco = item.css(".price__fraction::text").extract_first()

            if item.css(".price__decimals::text").extract_first():
                preco += "," + item.css(".price__decimals::text").extract_first()

            preco_produtos.append(preco)

        for nome, preco in zip(nomes_produtos, preco_produtos):
            yield {
                "nome" : nome,
                "preco" : preco
            }

        # Pergunta se tem a próxima página
        if response.css(".prefetch > span::text").extract_first() == "Próxima":
            yield scrapy.Request(url=response.css(".prefetch::attr(href)").extract_first(), callback=self.parse)