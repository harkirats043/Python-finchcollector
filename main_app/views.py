from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Finch

# Create your views here.
def get_finch_data():
    finches = [
    {'name': 'Canary Finch', 'color': 'Yellow', 'size': 'Small'},
    {'name': 'Bengalese Finch', 'color': 'Brown', 'size': 'Small'},
    {'name': 'Diamond Firetail Finch', 'color': 'Multicolored', 'size': 'Small'},
    {'name': 'Owl Finch', 'color': 'White and Gray', 'size': 'Small'},
    {'name': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'}
]
    return finches

def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def finches(request):
    finches = Finch.objects.all()
    return render(request,'finches/finches.html',{'finches':finches})

def finches_detail(request,finch_id):
    finch=Finch.objects.get(id=finch_id)
    return render(request,'finches/detail.html',{'finch':finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'