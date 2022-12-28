from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
def brock(request):
    form=StudentForm()
    d={'form':form}
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('inserting data is succesfull')
    return render(request,'brock.html',d)