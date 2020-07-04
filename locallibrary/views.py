from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): 

    nombre="sebitas"

    doc_externo=open("C:/locallibrary/locallibrary/locallibrary/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_":nombre})

    documento=plt.render(ctx) #renderizar

    return HttpResponse(documento)

def despedida(request): 
    return HttpResponse("chao Sebas")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y Hora %s
    </h1>
    </body></html>""" %fecha_actual
    
    return HttpResponse(documento)

def calcularEdad(request, agno):
    edadActual=18
    periodo=agno-2020
    edadFutura=edadActual+periodo
    documento="<html><body><h2> En el año %s tendras %s años"%(agno, edadFutura)

    return HttpResponse (documento)