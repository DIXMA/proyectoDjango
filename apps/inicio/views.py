from django.shortcuts import render_to_response
from .models import Busqueda
from django.http import HttpResponse
import json
from django.core import serializers
from TwitterSearch import *
import tweepy

def busqueda(request):
	return render_to_response('inicio/busqueda.html')

def listarHistorial(request):	
	nombre = request.GET.get("nombre","")
	palabra = Busqueda(nombre=nombre)
	palabra.save()
	#dataX = serializers.serialize('json',Busqueda.objects.order_by('-creado').distinct('nombre'))
	data = Busqueda.objects.order_by('-creado')
	lista = "<div class='panel panel-info'><div class='panel-heading'><h3 class='panel-title'>Historial de Busqueda</h3></div><ul class='media-list' style='overflow: scroll; width: 350px; height: 250px;'>"
	for palabra in data:
		lista += "<p>"+palabra.nombre+"</p>"
		print palabra.nombre
	lista += "</ul></div>"
	return HttpResponse(lista)
    
def listarTweets(request):
	nombre = request.GET.get("nombre","")
	consumer_key="mzR3Zogvriir7PN8LFKBkR4QG"
	consumer_secret="MPsQOACN3OsgdriwnD8SWB5tBu9qdBpmvNXj1isBstY2AIge34"
	access_token="582023897-kfhBGR5YpE8Ep5o0mIPJPYz1sGWrhC8oLs0bRzAZ"
	access_token_secret="T9mD6jIeArsSKjPdte9Bd28k1sXze1yqRqvFjPVjUW3EW"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)	
	busqueda = api.search(q=nombre,count=10, result_type='recent')
	lista = "<div class='panel panel-primary'><div class='panel-heading'><h3 class='panel-title'>Tweets</h3></div><ul class='media-list'>"
	for tweet in busqueda:
		#print busqueda
		lista += "<div class='breadcrumb'>"
		lista += "<li class='media'>"
		lista += "<a class='media-left' href='#'>"
		lista += "<img data-holder-rendered='true'  class='img-thumbnail' src="+tweet.user.profile_background_image_url+" style='width: 64px; height: 64px;' data-src='holder.js/64x64' alt='64x64'></img></a>"
		lista += "<div class='media-body'>"
		lista += "<h4 class='media-heading'>"+tweet.user.screen_name+"</h4>"
		lista += ""+tweet.text+"</div></li></div>"
	lista += "</ul></div>"
	return HttpResponse(lista)