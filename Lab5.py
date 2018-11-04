def TestYN(testInput):
    while(testInput != 'y' or 'n'):
        if(testInput == 'y'):
            return 1
        elif(testInput == 'n'):
            return 0
        else:
            testInput = input('uwotm8? ')

def ValidateContinue():
    userInput = input('Would you like to continue? (y/n)')
    if(TestYN(userInput) == 0):
        print('Goodbye!')
        exit()
    else:
        print('WOOOOOOOOOOOOOOO!!!!!!')

while(1):
    userInput = int(input('Enter an integer: '))
    factorial = 1
    i = 1
    while (userInput != 1):
        factorial *= userInput
        userInput -= 1

    print(str(factorial))
    ValidateContinue()