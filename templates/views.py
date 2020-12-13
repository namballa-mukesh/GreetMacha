from django.shortcuts import render
from .models import storedInformation
import json

# Create your views here.
def home(request):
	return render(request,"homepage/index.html",{})

def t1(request):

	if request.method=='POST':
		name=request.POST['bfname']
		message=request.POST['message']
		context={'name':name,'message':message}

	return render(request,"templates/birthday_template.html", context)