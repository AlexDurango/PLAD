import csv, random
from .encryptPLAD import lamdaN, generatePrivateKey
from .createPLAD import printPLADlogo

def main():    
    e = 65537
    oldData = []

    with open("./scripts/dbPLAD.csv", "r") as keys:
        reader = csv.reader(keys)
        oldData = [line for line in reader]

    
    p, q = getPrivateKeys()
    n = p*q
    publicKeys = [n,e]

    with open("./scripts/dbPLAD.csv", "w") as newKeys:
        writer = csv.writer(newKeys)
        writer.writerow(publicKeys)
        writer.writerows(oldData)


    landaN = lamdaN(p, q)
    private_key_d = generatePrivateKey(landaN, e)
    
    return p, q, private_key_d


def getPrivateKeys():

    rangeOfPrimes = input(" - What range of prime numbers do you want to use to choose your keys?\n\n\033[36m NOTE: We recomend to use a low range but to choose prime numbers that are far from each other.\n      If you increase the range, it will be more secure but the program should get slower.\n\033[37m\nRange (Minimun Value, Maximun Value) Ex: (100, 500):\n")
    rangeOfPrimes = rangeOfPrimes.replace("-",',').replace(" ",'').replace("(",'').replace(")",'').split(",")

    primeNumbers = []

    #Analiza si el número dado es primo o no, calculando el modulo desde el 2 hasta n-1
    def check(n):
        for i in range(2,n):
            if (n % i == 0):
                return False
        
        return True

    #Analiza un rango de números y entrega los que son primos
    try:
        for n in range(int(rangeOfPrimes[0]), int(rangeOfPrimes[1])):
            if check(n):
                primeNumbers.append(n)

    except:
        printPLADlogo()
        print("Invalid range, try something like: (200, 350)")
        exit(1)

    #print(primeNumbers)
    print("\n\n\nThis is the list of possible keys in the range that you gave:\n")
    print(primeNumbers)
    print("\nPlease write down two of them as your private keys.\n")
    print(" - - - - - - - - - - - - - - - - - - - - - - -\n\n")


    try:
        p = int(input("First key (P): "))
        q = int(input("Second key (Q): "))

    except:
        printPLADlogo()
        print("Invalid keys, try again!")
        exit(1)

    try:
        if (p < 1) or (q < 1):
            exit(1)
        if p not in (primeNumbers):
            exit(1)
        elif q not in (primeNumbers):
            exit(1)
        
        return p, q
    except:
        printPLADlogo()
        print("The keys are not in the range that you gave. Try again!")
        exit(1)
