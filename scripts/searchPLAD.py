import csv
from .createPLAD import printPLADlogo

def main(argv):
    searching_key_name = getRequirements(argv)
    CypherText = searchByKeyName(searching_key_name)
    return CypherText, searching_key_name


def getRequirements(argv):
    searching_key_name = ''

    if len(argv) == 3:
        searching_key_name = argv[2].lower()
        return searching_key_name

    elif len(argv) < 3:
        printPLADlogo()
        print("Don't forget to use a key name before the comand '-S'. Type -h for help.")
        exit(1)
    
    else:
        printPLADlogo()
        print("Unknown command. Try 'python3 PLAD.py -h' for help.")
        exit(1)
        

def searchByKeyName(searching_key_name):

    indexOfSearchingKeyName = -1
    CypherText = []

    with open("./scripts/dbPLAD.csv", "r") as searchingFile:
        reader = csv.reader(searchingFile)
        data = [line for line in reader]

        for i in range(0, len(data)):
            if searching_key_name == data[i][1]:
                indexOfSearchingKeyName = i
        
        if indexOfSearchingKeyName == -1:

            printPLADlogo()
            print("Key name didn't found on the data base. Please check and try again!\n")
            exit(1)

        CypherText = data[indexOfSearchingKeyName][2]
    
    return CypherText
