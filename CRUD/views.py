from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Voila</h1>")

import pymongo
client = pymongo.MongoClient('mongodb+srv://ishaan:masterPassword%400108@trialcluster.spns5qz.mongodb.net/?retryWrites=true&w=majority')
dbname = client['movies']
collection=dbname['entertainment']

entertainment_1={
    "name": "The Big Bang Theory",
    "img": "NA",
    "summary": "Comedy Series"
}

collection.insert_one(entertainment_1)
ent_deets = collection.find({})
for r in ent_deets:
    print(r['name'])

