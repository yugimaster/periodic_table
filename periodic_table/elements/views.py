from django.shortcuts import render
import json

def index(request):
    data = get_local_json()
    return render(request, 'index.html', {"ElementData": data})

def get_local_json():
    with open("elements/static/json/periodic.json", 'r') as f:
        data = json.load(f)
        return data['elements']
