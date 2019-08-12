import requests
from django.shortcuts import render
import datetime
from decouple import config

# Create your views here.
def home(request):
    title = "Restaurant table"
    url = config('url')
    
    transactions = requests.get(url.format()).json()

    table = transactions["records"]

    # to convert the time format
    for i in table:
        i["fields"]["Timestamp"]= datetime.datetime.strptime(i["fields"]["Timestamp"],'%Y-%m-%dT%H:%M:%S.000Z').strftime('%d-%m-%Y')

    branches_dict={}

    for i in table:
        # removes branch duplicates and stores them as dictionaries 
        if i["fields"]["Branch"] not in branches_dict:
            branches_dict[i["fields"]["Branch"]]=[]

        # to have all the the amounts in their respective branches
        if i["fields"]["Branch"] in branches_dict:
            for j in branches_dict:
                if j==i["fields"]["Branch"]:
                    branches_dict[j].append(i["fields"]["Amount"])  

    # to get the highest amount per branch
    for j in branches_dict:
        branches_dict[j]=max(branches_dict[j])
    
        # to check the highest spender per branch and highlight them
        for i in table:
            if i["fields"]["Amount"]== branches_dict[j]:
                i["fields"]["high"]= f"Top in {i['fields']['Branch']}"

    return render(request,'home.html',{'title':title, 'table':table})
    

  