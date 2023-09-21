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
         {
            'name': 'Java Sparrow',
            'scientific_name': 'Lonchura oryzivora',
            'description': 'Small bird with gray plumage and pink beak.',
            'habitat': 'Grasslands, agricultural fields, and urban areas of Java.'
        },
        {
            'name': 'Society Finch',
            'scientific_name': 'Lonchura domestica',
            'description': 'Small and social bird known for its singing ability.',
            'habitat': 'Originally from Southeast Asia, now kept as a pet worldwide.'
        },
        {
            'name': 'Star Finch',
            'scientific_name': 'Neochmia ruficauda',
            'description': 'Colorful bird with red head and tail.',
            'habitat': 'Open woodlands, grasslands, and scrublands of Australia.'
        }
    ]
    return finches

def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def finches(request):
    return render(request,'finches/finches.html',{'finches':finches})