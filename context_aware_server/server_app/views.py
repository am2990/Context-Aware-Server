from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def store(request):
	if request.method == 'POST':
		# print "POST request has come"
		# Parse data using request.body
		# json parse
		# parse and store in Database!

	return render(request, "server_app/index.html")

	#parse data obtained as needed.
