from django.shortcuts import render
from mysite.models import Product,Customer
from . import forms
def index (request):
    customer = Customer.objects.all
    my_dict = {'customers':customer}
    return render(request, 'index.html' , context= my_dict)

def form_name_view(request):
    form = forms.ForName()
    return render(request,'form.html',{'form':form})
