
#Atividade de WebScrapping
#Alunas: Caroline Galiza e Marcela Carvalho
#Questão 01 - > Cotação do dolar na uol. 


# Comando de execução do projeto: scrapy runspider cotacaodolaruol.py --nolog

#Importando Scrapy
import scrapy 

#Criando a classe CotacaoDola
class CotacaoDolarUol(scrapy.Spider):
    #Definido o nome da classe e passando a URL do site da UOL para que ele seja crawleado
    name = "cotacao-dolar-uol"
    start_urls = [
        "https://www.uol.com.br/"
    ]

    #Desabilitando o log 
    custom_settings = {
        "LOG_ENABLED" : False
    }
    

    #Criando o método parse
    def parse(self, response):
        #Capturando e printando o valor do dólar
        #Usando o método response para acessar o valor do dolar 
        dolar = response.css(".currency_quote__down::text").extract_first()
        print("A cotação atual do dólar é: {}".format(dolar))

