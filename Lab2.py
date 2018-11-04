import re
from decimal import Decimal

def testYN(userInput):
    # Why does this one work and the other one doesn't?
    while(userInput != 'y' or 'n'):
        if(userInput == 'y'):
            return 1
        elif (userInput == 'n'):
            return 0
        else:
            userInput = input("I don't understand. Try again!")
    
    # This one doesn't work how I want it to. Why?
    # while (userInput != 'y' or 'n'):
    #     userInput = input("I don't understand. Try again!")
    #     continue

    # if(userInput=='y'):
    #     return 1
    # elif(userInput=='n'):
    #     return 0

def promptContinue():
    testInput = input('Would you like to continue?')
    if (testYN(testInput) == 0):
        print('Goodbye')
        exit()
    else:
        print('Bodacious! Let\'s continue then!')

def getRoomDimension(numberRegex, dimension):
    toReturn = input('What is the ' + dimension + ' of the room?')
    while (1):
        if (numberRegex.match(toReturn)):
            return toReturn
        else:
            toReturn = input('That wasn\'t a number! Try again!')

numberRegex = re.compile('^([0-9]{1,}.[0-9]{1,})|[0-9]{1,}$')
print('Hello! Welcome to the Room Detail Generator!')
    
while(1):
    length = Decimal(getRoomDimension(numberRegex, 'length'))
    width = Decimal(getRoomDimension(numberRegex, 'width'))
    height = Decimal(getRoomDimension(numberRegex, 'height'))
    print('The perimeter of the room is: %s' %(length*2 + width*2))
    print('The area of the room is: %s' %(length*width))
    print('The volume of the room is: %s' %(length*width*height))
    promptContinue()