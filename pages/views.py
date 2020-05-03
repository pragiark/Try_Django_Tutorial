from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>") # stiong of htmlcode
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about as",
        "this is true": True,
        "my_number": 7,
        "my_list": [7, 77, 777, 7777, "ABC"]
    }
    return render(request, "about.html", my_context)

def spcial_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")