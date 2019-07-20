import requests
from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    title = "Restaurant table"
    url = 'https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU'
    
    transactions = requests.get(url.format()).json()

    table = transactions["records"]
   
    return render(request,'home.html',{'title':title, 'table':table})
    