from django.shortcuts import render

# Create your views here.
def get_finch_data():
    finches = [
        {
            'name': 'Zebra Finch',
            'scientific_name': 'Taeniopygia guttata',
            'description': 'Small, colorful bird native to Australia.',
            'habitat': 'Open grasslands, savannas, and forests.'
        },
        {
            'name': 'Gouldian Finch',
            'scientific_name': 'Erythrura gouldiae',
            'description': 'Brightly colored bird with distinctive head colors.',
            'habitat': 'Northern Australia, particularly in savannas.'
        },
        # Add more finches as needed
    ]
    return finches

def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')
