from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Restaurant table"

    return render(request,'home.html', {"title":title})
    