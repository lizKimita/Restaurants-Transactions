import requests
from django.shortcuts import render


# Create your views here.
def home(request):
    title = "Restaurant table"
    url = 'https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU'
    
    transactions = requests.get(url.format()).json()
   
    restaurant_table = {
        "name":transactions['records'][0]['fields']['Name'],
        "amount":transactions['records'][0]['fields']['Amount'],
        "timestamp":transactions['records'][0]['fields']['Timestamp'],
        "branch":transactions['records'][0]['fields']['Branch']


       
    }
    table = {"restaurant_table":restaurant_table}
    
    return render(request,'home.html', table)
    