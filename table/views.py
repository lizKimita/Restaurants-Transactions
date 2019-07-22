import requests
from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    title = "Restaurant table"
    url = 'https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU'
    
    transactions = requests.get(url.format()).json()

    table = transactions["records"]
    date = [];
    for i in table:
        time =i["fields"]["Timestamp"]
        newtime = datetime.datetime.strptime(time,"%Y-%m-%dT%H:%M:%S.000Z").strftime('%d-%m-%Y')
        date.append(newtime)
    print(time)
   
    return render(request,'home.html',{'title':title, 'table':table, 'date':date})

    # for i in table:
    #     date = [];
    #     time = i["fields"]["Timestamp"]
    #     newtime = datetime.datetime.strptime(time,"%Y-%m-%dT%H:%M:%S.000Z").strftime('%d-%m-%Y')
    #     date.append(newtime)

    #     new = ",".join(date)
    
    #     locations = []
    #     branch = i["fields"]["Branch"]
    #     for x in branch:
    #         if x not in locations:
    #             locations.append(branch)

    #     print(branch)
   
    # return render(request,'home.html',{'title':title, 'table':table, 'date':date})
    