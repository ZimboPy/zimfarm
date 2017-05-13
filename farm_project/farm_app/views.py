from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponseRedirect


from datetime import datetime


def home(request):
	return render(request,'farm_app/index.html')

# Create your views here.
