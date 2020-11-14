import sys, pyfiglet, csv 

from scripts import createPLAD, deletePLAD, writePLAD, searchPLAD, encryptPLAD, decryptPLAD, set_keys
from sys import argv

def main():

    with open("./scripts/dbPLAD.csv", "r") as public_keys:
        reader = csv.reader(public_keys)
        oldData = [line for line in reader]
        n = int(oldData[0][0])

        if n == -1:
            printPLADlogo()
            print("Welcome to PLAD, your secure password manager. First of all, we are going to set our private keys.\n")

            p, q, private_key_d = set_keys.main()

            try:
                print("\n\n - - - - - - - - - - - - - - - - - - - - - - -")
                print(f"Your first key (P) is {p}\nYour second key (Q) is: {q}\nYour MASTER password (D) is: {private_key_d}\n\n")
                print('\033[31m'+"° Make sure you can remeber these or try to write them down on a papper. °\033[37m")
                print(" - - - - - - - - - - - - - - - - - - - - - - -")
                print("\n Now, run PLAD.py -h and see the instructions to create your own PLAD!")
                print("\n"*2 + "Created by QWERTY")
                exit(0)
            except:
                print("\n")
        else:
            e = int(oldData[0][1]) 

            #Imprimir usage
            if (len(argv) < 2 or (argv[1] not in ("-C, -D, -S, -L, -V"))):
                printIntroductionComands()
                exit(1)

            #If the second argument in the comand line is -C it williniciate the process to create a PLAD
            elif argv[1] == '-C':

                try:
                    #inicia la creación de la PLAD y da el argumento argv que son las condiciones que dió el usuario
                    RandomPassword, key_name = createPLAD.main(argv)
                    try:
                        Cypher_Text, private_key_d = encryptPLAD.main(RandomPassword, n, e)
                        print("\n\n - - - - - - - - - - - - - - - - - - - - - - -")
                        print(f"The password generated is:\033[34m {RandomPassword}\033[37m ")
                        print(f"Remember that the private MASTER key for {key_name} is: {private_key_d}") 
                        print(" - - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n"*2 + "Created by QWERTY")
                        try:
                            writePLAD.writeOnTheFile(key_name, Cypher_Text)
                        except:
                            printPLADlogo()
                            print(" Error writting on .csv")
                    except:
                        printPLADlogo()
                        print(" Please give valid keys :C")
                except:
                    printPLADlogo()
                    print(" Unknown command. Try 'python3 PLAD.py -h' for help.")

            elif argv[1] == '-S':
                            
                with open("./scripts/dbPLAD.csv", "r") as check_db:
                    reader = csv.reader(check_db)
                    oldData = [line for line in reader]
                if len(oldData) < 3:
                    printPLADlogo()
                    print("\n You haven't created a PLAD yet. Try PLAD.py -h for instructions.")
                    exit(1) 
                try:
                    resulted_cypher_text, KeyName = searchPLAD.main(argv)
                    plain_password = decryptPLAD.main(n, e,resulted_cypher_text)
                    printPLADlogo()
                    print("\n\nThe password for "+KeyName+" is: \n\n"+plain_password)
                    print("\n"*2 + "Created by QWERTY")
                except:
                    print("\n")

            elif argv[1] == '-D':
                try:
                    if argv[2] == "admin":
                        exit(1)
                    try:
                        deletePLAD.main(argv, n, e)
                    except:
                        print("\n")
                except:
                    print("\n You can't delete the admin, or the admin will delete you ...\n")
                
            elif argv[1] == '-L':
                with open("./scripts/dbPLAD.csv", "r") as database:
                    database = csv.reader(database)
                    oldData = [line for line in database]
                
                if len(oldData) < 3:
                    printPLADlogo()
                    print("\n You haven't created a PLAD yet. Try PLAD.py -h for instructions.")
                    exit(1)
                
                del(oldData[0])
                del(oldData[0])
                printPLADlogo()
                print(" The keynames on the database are: \n")
                for i in range(len(oldData)):
                    print(f" {i+1}- {oldData[i][1]}")
                
                print("\nCreated by QWERTY")
            
            elif argv[1] == '-V':
                print("PLAD 1.0.0")                
                    

#Print the PLAD logo
def printPLADlogo():
    print("\n\n - - - - - - - - - - - - - - - - - - - - - - -")
    ascii_logo = pyfiglet.figlet_format("PLAD")
    print(ascii_logo)    


#This function will print the usage and the basics commands
def printIntroductionComands():
    printPLADlogo()
    print("Usage: \n\n ")
    print(" -C <key name> <N° characters> <S+ or S-> ==> Create a new PLAD using a key name, the lenght of the password and the usage of symbols.\n")
    print(" -S <key name> ==> Search a PLAD using it's keyname to get it's password. \n")
    print(" -D <key name> ==> Delete a PLAD by it's keyname.\n")
    print(" -L ==> List all the keynames on the database. \n")
    print(" -V ==> Print currently PLAD version.\n")
    print(" -h ==> Print this list of comands.\n")
    print(" \n Example: python3 PLAD.py -C john.doe@gmail.com 15 S+\n          python3 PLAD.py -S john.doe@gmail.com")
    print("\n"*2 + "Created by QWERTY")
    
if __name__ == '__main__':
    main()