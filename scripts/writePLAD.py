import csv


def writeOnTheFile(key_name, cypher_text): 

    #Le asigna un index a el nuevo PLAD que está siendo creado
    actualIndex = 1

    #En esta lista se va a guardar la información del archivo .csv ya existente
    oldData = []

    #Lee el archivo y guarda la información en la lista oldData
    with open("./scripts/dbPLAD.csv", "r") as old_plad:
        reader = csv.reader(old_plad)
        oldData = [line for line in reader]
    
    #Lee nuevamente el archivo para asignar un index nuevo al plad que se está crando

    with open("./scripts/dbPLAD.csv", "r") as new_index:
        indexReader = csv.reader(new_index)

        next(indexReader) #Adelanta una linea para evitar leer la linea index, key_name, cypher_text
        for lastIndex in indexReader:
            
            '''
            IMPORTANTE: El archivo .csv no puede dejar lineas en blanco, de otro modo nos dará un error
            '''
    
            if int(lastIndex[0]) >= actualIndex:
                actualIndex += 1

    #Construye los elementos del nuevo PLAD
    newPladRow = [str(actualIndex), key_name, cypher_text]
    
    #Agrega la información antigua y luego agrega una nueva linea con la información que se está dando
    with open("./scripts/dbPLAD.csv", "w") as new_plad:
        plad_writer = csv.writer(new_plad, delimiter = ',')
        plad_writer.writerows(oldData)
        plad_writer.writerow(newPladRow)
