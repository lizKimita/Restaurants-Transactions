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


    return render(request,'home.html',{'title':title, 'table':table, 'date':date})
    

    # branch = i["fields"]["Branch"]
    # amount = i["fields"]["Amount"]
    # appended = "**Top in {branch}**"

    # for n in range (len(branch)):
    # if branch[n] == branch[n+1] and amount[n] > amount[n+1] or amount[n+1] > amount[n]:
    #     print (branch)

    # return render(request,'home.html')