import requests
from django.shortcuts import render


# Create your views here.
def home(request):
    title = "Restaurant table"
    url = 'https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU'
    
    transactions = requests.get(url.format()).json()
   

    restaurant_table = {
        "name":transactions['Name'],

    }
    print(restaurant_table)

    return render(request,'home.html', {"title":title})
    