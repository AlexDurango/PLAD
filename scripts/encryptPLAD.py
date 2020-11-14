import random, string
from .createPLAD import printPLADlogo


def main(RandomPassword, n, e):
    password_ASCII_list = ToASCII(RandomPassword)
    p,q = recivesKeys(n)
    landaN = lamdaN(p,q)
    private_key_d = generatePrivateKey(landaN, e)
    Cypher_Text = toCypherText(password_ASCII_list, n, e)
    return Cypher_Text, private_key_d
    

#Pass the random password to ASCII in a array for each word
def ToASCII(password):
    password_ASCII = []

    for i in range(0,len(password)):
        password_ASCII.append(ord(password[i]))
    
    return password_ASCII


#Recive the necesary values for P and Q, the numbers of N
def recivesKeys(n):
    printPLADlogo()
    
    p = int(input(" - Wich is the first key (P)?: \n"))
    q = int(input(" - Wich is the second key (Q)?: \n"))     

    if p*q == n:
        return p, q
    else:
        exit(1)


#Calculate the LCM of P-1 and Q-1
def lamdaN(p, q):
    landaN = 0
    p = p-1
    q = q-1

    #De esta manera se calcula el m.c.m de dos números
    landaN = max(p,q)
    while True:
        if (landaN % p == 0) and (landaN % q == 0):
            return landaN
        
        landaN += 1


#Pasa de ascii a texto cifrado con el metodo RSA
def toCypherText (password_ASCII, n, e):

    CypherText = []

    for i in range(0, len(password_ASCII)):
        CypherText.append((password_ASCII[i]**e) % n)
    
    return CypherText


def generatePrivateKey(landaN, e):
    d = 1
    for i in range(1, landaN):
        d = i
        #Esta ecuación permite conocer el valor de la llave d
        if (d * e)%landaN == 1:
            return d