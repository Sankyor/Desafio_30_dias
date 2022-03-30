#3. Create a Contact List and Persist in JSON
##27-03-2022
#Ref: https://www.geeksforgeeks.org/append-to-json-file-using-python/

import json
file_data = []

with open("Dia3.json", "r+") as outfile:
    try:
        file_data = json.load(outfile)
        print("Se cae acá")
        for datos in file_data["Contactos"]:
            print(datos)
    except Exception as e:
        file_data = {"Contactos":[]}  
        print("No hay registros")
    finally:
        nombre = str(input("Por favor ingrese el nombre del contacto nuevo: "))
        numero = str(input("Por favor ingrese el nombre del contacto: "))             
        
        # Data to be written
        dictionary ={
            "nombre" : nombre,
            "numero" : numero
        }
        json_object = json.dumps(dictionary, indent = 2)
        file_data["Contactos"].append(dictionary)
        outfile.seek(0)
        print("Nuevo dato a insertar: ", dictionary)
        json.dump(file_data, outfile, indent = 2)
