import matplotlib
matplotlib.use('Agg')

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

import matplotlib.pyplot as plt
import io, urllib, base64

import random as random

from .models import Produto

# Create your views here.
def index(request):
    
    def generateMockData():
        
        #Data array
        productsArray = []

        product1 = Produto
        product1.productName = 'Teclado'
        
        productsArray.append(product1)
        
        product2 = Produto
        product2.productName = 'Mouse'

        productsArray.append(product2)

        product3 = Produto
        product3.productName = 'GPU'

        productsArray.append(product3)

        product4 = Produto
        product4.productName = 'Placa-Mae'
        
        productsArray.append(product4)

        return productsArray



    def generateSalesGraph():
        #Gerando o grafico de volume de vendas
        
        products = generateMockData()
        meses = ['Jan/2020', 'Fev/2020', 'Mar/2020', 'Abr/2020', 'Mai/2020', 'Jun/2020']

        for product in products:
            sales = []
            for i in range(6):
                sales.append(random.randint(10, 250))

            plt.plot(meses, sales, marker='o', linestyle='-', label=product.productName)

        plt.xlabel('Mês')
        plt.ylabel('Lotes')
        plt.title('Gráfico de venda de lotes de produto')
        
        return plt.gcf()


    def generateProductPie():

        labels = 'GPU', 'Placa-Mãe', 'Teclado', 'Mouse'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax1.axis('equal') 

        plt.title('Gráfico de Tipos de Produtos em Estoque')

        return plt.gcf()


    sales = generateSalesGraph()
    product = generateProductPie()

    #Serializando imagem
    buffer = io.BytesIO()
    sales.savefig(buffer, format='png')
    
    buffer.seek(0)

    salesString = base64.b64encode(buffer.read())
    salesUri = urllib.parse.quote(salesString)

    buffer = io.BytesIO()
    product.savefig(buffer, format='png')

    buffer.seek(0)

    productString = base64.b64encode(buffer.read())
    productUri = urllib.parse.quote(productString)

    #Montando a view
    template = loader.get_template('integrador/index.html')
    context = {'salesUri':salesUri, 'productUri':productUri}

    plt.close(sales)
    plt.close(product)

    return HttpResponse(template.render(context, request))
    