import requests
import json 

def get_docs(ruta):
    req = requests.get(ruta) 

    if req.status_code == 200: 
       dic =  json.loads(req.text) 
       return dic 

def get_data_sw_character():
    
    sw_data = [] 

    result = get_docs("https://swapi.dev/api/people/") 
    while(result["next"] is not None):
        for doc in result["results"]:
            #print(doc["name"])
            sw_data.append(doc)
        #print(result["next"])
        #a = input()     
        result = get_docs(result["next"])
    
    return sw_data

def busqueda(vector, bus):
    pos = None

    for i in range(0, len(vector)):
        if(vector[i] == bus):
            pos = i

    return pos 

def filtrado():

    sw_data = []

    result = get_docs("https://swapi.dev/api/people/") 
    while(result["next"] is not None):
        for doc in result["results"]:
            sw_data.append(doc) 
        result = get_docs(result["next"])  
    return sw_data      
    