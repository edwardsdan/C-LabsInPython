from StudentClass import Student

def MakeList():
    toReturn = []
    for i in range(10):
        toReturn[i] = GetStudentInfo()

def GetStudentInfo():
    name = input('What is their name? ')
    age = int(input('How old are they? '))
    home = input('Where do they live? ')
    food = input('What do they like to eat? ')
    return Student(name,food,home,age)