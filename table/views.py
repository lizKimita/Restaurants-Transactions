import requests
from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    title = "Restaurant table"
    url = 'https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU'
    
    transactions = requests.get(url.format()).json()

    table = transactions["records"]

    for i in table:
        i["fields"]["Timestamp"]= datetime.datetime.strptime(i["fields"]["Timestamp"],'%Y-%m-%dT%H:%M:%S.000Z').strftime('%d-%m-%Y')


    return render(request,'home.html',{'title':title, 'table':table})
    

    branch = i["fields"]["Branch"]
    amount = i["fields"]["Amount"]
    appended = "**Top in {branch}**"

    for n in range (len(branch)):
        if branch[n] == branch[n+1] and amount[n] > amount[n+1] or amount[n+1] > amount[n]:
            print (branch)

    return render(request,'home.html')