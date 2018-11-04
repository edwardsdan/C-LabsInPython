import re

def TestYN(userInput):
    while(userInput != 'y' or 'n'):
        if(userInput == 'y'):
            return 1
        elif(userInput == 'n'):
            return 0
        else:
            userInput = input('I don\'t understand! Try again!')

def PromptContinue():
    testInput = input('Would you like to continue? (y/n)')
    if(TestYN(testInput) == 0):
        print('Goodbye!')
        exit()
    else:
        print('Woohoo!')

def ValidateNumber():
    numberRegex = re.compile('^[1-9][0-9]$|^[1-9]$')
    userInput = input('Enter an integer less than 100 but greater than 0: ')
    while not(numberRegex.match(userInput)):
        userInput = input('uwotm8? ')
    return int(userInput)


while(1):
    userInput = ValidateNumber()
    i = 1
    print('Number\t\tSquared\t\tCubed')
    for i in range(1,userInput+1):
        print(str(i) + '\t\t' + str(i**2) + '\t\t' + str(i**3))
    PromptContinue()