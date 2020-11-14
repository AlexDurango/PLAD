import random, string, pyfiglet


#Print the PLAD logo
def printPLADlogo():
    print("\n\n - - - - - - - - - - - - - - - - - - - - - - -")
    ascii_logo = pyfiglet.figlet_format("PLAD")
    print(ascii_logo)


def main(argv):
    key_name, number_characters, usage_symbols = get_requirements(argv)
    RandomPassword = generate_random_password(number_characters, usage_symbols)
    return RandomPassword, key_name


#Gets the requirements for the command -C
def get_requirements(argv):

    #Declare the 3 variables needed for creating a new PLAD
    key_name = "error"
    number_characters = -69
    usage_symbols = "error"

    if len(argv) == 5:    
        
        #Set the key name of the PLAD as the 3th argument
        key_name = argv[2]

        #Set the number of caracters as the 4th argument the user gave us, in case it isn't a number in base 10
        number_characters = int(argv[3])

        #Check if the user gave permision to use symbols or not
        if argv[4] not in ("S+, S-, s+, s-") or number_characters < 1:
            exit(1)

        elif (argv[4] in ("S+, s+")):
            usage_symbols = True
            
        elif (argv[4] in ("S-, s-")):
            usage_symbols = False

        #Returns the 3 variables needed for creating the PLAD
        return key_name.lower(), number_characters, usage_symbols
    
    else: 
        exit(1)


def generate_random_password(number_characters, usage_symbols):
    
    password = ''

    if usage_symbols == True:

        #List of printable characters that include symbols
        password_characters = string.ascii_letters + string.digits + string.punctuation
        
        #Generate a random password
        password = ''.join(random.choice(password_characters) for i in range(number_characters))

        #Shuffle the last password to make it more random xd
        for i in range(0, number_characters):
            password = ''.join(random.sample(password, len(password)))
            
        return password
    
    elif usage_symbols == False:
        
        #List of printable characters that include symbols
        password_characters = string.ascii_letters + string.digits  # + string.punctuation ya que no admite los simbolos
        
        #Generate a random password
        password = ''.join(random.choice(password_characters) for i in range(number_characters))

        #Shuffle the last password to make it more random xd
        for i in range(0, number_characters):
            password = ''.join(random.sample(password, len(password)))
            
        return password