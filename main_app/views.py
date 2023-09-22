from django.shortcuts import render

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
    return render(request,'finches/finches.html',{'finches':finches})