import re

class Testing:
    
    @staticmethod
    def TestRegex(regexPattern, userInput):        
        while not (regexPattern.match(userInput)):
            userInput = input('That input was not valid! Try again! ')
        print('Input was valid!')

    @staticmethod
    def TestName():
        userInput = input('Enter a valid name: ')
        nameRegex = re.compile(r'^[A-Z]{1}[a-z]{1,29}$')
        Testing.TestRegex(nameRegex, userInput)

    @staticmethod
    def TestEmail():
        userInput = input('Enter a valid email: ')
        emailRegex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        Testing.TestRegex(emailRegex, userInput)

    @staticmethod
    def TestPhone():
        userInput = input('Enter a valid phone #: ')
        phoneRegex = re.compile(r'^\d{10}$|^\d{3}-\d{3}-\d{4}$')
        Testing.TestRegex(phoneRegex, userInput)

    @staticmethod
    def TestDate():
        userInput = input('Enter a valid date: ')
        dateRegex = re.compile(r'^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/((0001)|[1-9]{4})$')
        Testing.TestRegex(dateRegex, userInput)


def TestContinue():
    userInput = input('Would you like to continue? (y/n) ')
    if (TestYN(userInput) == 0):
        print('Goodbye!')
        exit()
    print('WOOOOOOOOOOOOO!!!!!!!!!!!')

def TestYN(userInput):
    while(1):
        if(userInput == 'y'):
            return 1
        elif(userInput == 'n'):
            return 0
        else:
            userInput = input('I don\'t understand! Try again! ')
    

def Run():
    while(1):
        Testing.TestName()
        Testing.TestEmail()
        Testing.TestPhone()
        Testing.TestDate()
        TestContinue()

Run()