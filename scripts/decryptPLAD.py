from .createPLAD import printPLADlogo


def main(n, e,cypher_text):

    #Recives the privates keys from the user
    p, q, private_key_d = recivesKeys(n)

    #Analize if the keys are correct, if they aren't it just send an error message
    correct_key_d = analizePrivateMaterKey(n, e, p, q, private_key_d)

    if correct_key_d == True:
        plain_password = toPlainText(cypher_text, private_key_d, n)
        return plain_password
    else:
        print("The Master Key is incorrect, try again!") 
        exit(1)
 

def recivesKeys(n):
    printPLADlogo()
    
    p = int(input(" - Wich is the first key? (P): \n")) 
    q = int(input(" - Wich is the second key? (Q): \n")) 
    private_key_d = int(input(" - Wich is the Master key? (D): \n"))    

    if p*q == n:
        return p, q, private_key_d
    else:
        printPLADlogo()
        print("Inavlid keys (P or Q). Try again!")
        exit(1)


def analizePrivateMaterKey(n, e, p, q, private_key_d):

    correct_key_d = False
    landaN = 0
    p = p-1
    q = q-1

    #De esta manera se calcula el m.c.m de dos números
    landaN = max(p,q)
    while True:
        if (landaN % p == 0) and (landaN % q == 0):
            break
        
        landaN += 1

    if (private_key_d*e) % landaN == 1:
        correct_key_d = True
        return correct_key_d 

    else:
        return correct_key_d


def toPlainText(cypher_text, private_key_d, n):

    #All this variables and lists are necessary for the decrypt
    plain_password = ''
    string_to_replace = ''
    list_plain_text = []
    list_plainText_ASCII= []
    
    #.csv files saves lists as complete strings, that's why we gotta delete symbols to leave just the number
    string_to_replace = cypher_text.replace('[','').replace(']','').replace(',','')

    #Put the cypher text into a list
    list_to_replace = string_to_replace.split()

    #PASAR DE CYPHER A PLAIN TEXT INGRESANDO CADA ELEMENTO DEL ARRAY A PLAIN TEXT
    for i in range(len(list_to_replace)):

        #This is the formula to decrypt the cypher text
        list_plain_text.append((int(list_to_replace[i])**private_key_d)%n)

        #Pass the decypted numbers into characters
        list_plainText_ASCII.append(chr(list_plain_text[i]))

        #Add thoses characters into a single variable
        plain_password = ''.join(list_plainText_ASCII)

    return plain_password