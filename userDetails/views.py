from django.shortcuts import render
from .models import formInformation
from templates.models import storedInformation
import json

# Create your views here.

def formpage(request):
	
	return render(request,'userDetailsPage/userDetailsForm.html',{})

def bdaypage(request):
	'''
	if request.method=="POST":
		user=request.user
		name=request.POST['name']
		email=request.POST['email']
		message=request.POST['message']
		picture=request.POST['filename']
		bname=request.POST['bfname']
		info = 	{'name':bname, 'message': message,'photo':picture}
		info= json.dumps(info)
		print(request.POST)

		ins = storedInformation(rid=user, forminfo=info)
		ins.save()'''
	return render(request, 'userDetailsPage/new 1.html',{})	