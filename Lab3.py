import re

def TestYN(userInput):
    while(userInput != 'y' or 'n'):
        if(userInput == 'y'):
            return 1
        elif(userInput == 'n'):
            return 0
        else:
            userInput = input('I do not understand that. Try again!')

def ValidateNumber():
    numberRegex = re.compile('^(100)$|^([1-9][0-9])$|^[1-9]$')
    testInput = input('Please enter a number between 1 and 100: ')
    while(1):
        if(numberRegex.match(testInput)):
            return int(testInput)
        else:
            testInput = input('That wasn\'t right! Try again!')

def PromptContinue():
    testInput = input('Would you like to continue? (y/n)')
    while(1):
        if(TestYN(testInput) == 0):
            print('Goodbye!')
            exit()
        else:
            print('Most excellent!')

def PrintConditions():
    userInput = ValidateNumber()
    if (userInput % 2 == 0):
        if(userInput >= 2 and userInput < 25):
            print('Even and less than 25')
        elif(userInput >= 26 and userInput <= 60):
            print('Even')
        else:
            print(userInput, "Even")
    else:
        if(userInput<=59):
            print('Odd')
        else:
            print(userInput, 'Odd')

while(1):
    PrintConditions()
    PromptContinue()
