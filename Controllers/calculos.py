
import json


with open("meteorites_data.json", "r", encoding= "utf-8") as f:
    datos = json.load(f)
    meteoro = datos["neos"]
    for metodo in datos["neos"]:
        print(metodo["name"])


def Listameteoros(datos):
    names = []
    for metodo in datos["neos"]:
        print(metodo["name"])
        names.append(metodo["name"])  
    return json(names)


def infoasteroide(datos, name):
    for metodo in datos["neos"]:
        if name == metodo["name"]:

            return json(metodo["neos"])


def lista_mayor_impacto():
    lista = datos["neos"][:]
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["impact"] < key["impact"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    
    top5 = lista[:5]
    return json(top5)





    
