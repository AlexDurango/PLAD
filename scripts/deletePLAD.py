import csv
from .createPLAD import printPLADlogo
from .decryptPLAD import recivesKeys, analizePrivateMaterKey

def main(argv,n,e):
    key_name_to_delete = getRequirements(argv)
    p, q, private_key_d = recivesKeys(n)
    correct_key_d = analizePrivateMaterKey(n, e, p, q, private_key_d)

    if correct_key_d == True:
        try:
            deleteByKeyName(key_name_to_delete)
            printPLADlogo()
            print(f"\nThe PLAD '{argv[2]}' was successfully removed!\n")

        except:
            print("\nThe keyname wasn't found on the data base. Please check and try again!")

    else:
        print("\nThe Master Key is incorrect, try again!") #MEJORAR
        exit(1)


def getRequirements(argv):
    searching_key_name = ''

    if len(argv) == 3:
        searching_key_name = argv[2].lower()
        return searching_key_name

    elif len(argv) < 3:
        printPLADlogo()
        print("Don't forget to use a key name before the comand '-D'. Type -h for help.")
        exit(1)
    
    else:
        printPLADlogo()
        print("Unknown command. Try 'python3 PLAD.py -h' for help.")
        exit(1)


def deleteByKeyName(searching_key_name):

    key_name_in_db = False
    indexOfKeyName = -1
    oldData = []

    with open("./scripts/dbPLAD.csv", "r") as searchingFile:
        reader = csv.reader(searchingFile)
        oldData = [line for line in reader]

        for i in range(0, len(oldData)):
            if searching_key_name == oldData[i][1]:
                key_name_in_db = True
                indexOfKeyName = i
                break
        
        if key_name_in_db == False:
            exit(1)

    del(oldData[indexOfKeyName])

    with open("./scripts/dbPLAD.csv","w") as new_file:
        writer = csv.writer(new_file)
        writer.writerows(oldData)

    return 