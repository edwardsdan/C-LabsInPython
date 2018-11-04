import random
import re

class DiceRoller:
    def isValidDice(self):
        userInput = input('How many sides for this dice? (even, <= 20) ')
        sidesRegex = re.compile('^[468]$|^[1][02468]$|^20$')
        while not (sidesRegex.match(userInput)):
            userInput = input('uwotm8? Try again! ')
        return int(userInput)

    def isInt(self):
        userInput = input('How many dice do you want to roll? (<=20) ')
        numberRegex = re.compile('^[1-9]$|^1[0-9]$|^20$')
        while not (numberRegex.match(userInput)):
            userInput = input('uwotm8? Try again! ')
        return int(userInput)

    def RollDice(self, diceList, rolls):
        print(f'Roll #{rolls}:')
        for die in diceList:
            print(random.randint(1,die))
            
    def AskRollDice(self, diceList, rolls):
        promptRoll = input('Would you like to roll now? (y/n) ')
        if(TestYN(promptRoll) == 1):
            self.RollDice(diceList, rolls)
            return 1

def TestYN(testInput):
    while(testInput != 'y' or 'n'):
        if(testInput == 'y'):
            return 1
        elif(testInput == 'n'):
            return 0
        else:
            testInput = input('uwotm8? ')

def ValidateContinue():
    userInput = input('Would you like to continue? (y/n) ')
    if(TestYN(userInput) == 0):
        print('Goodbye!')
        exit()
    else:
        print('WOOOOOOOOOOOOOOO!!!!!!')

def Game():
    GameRunner = DiceRoller()
    rolls = 1
    while(1):
        diceList = [0 for i in range(GameRunner.isInt())]
        i = 0
        while (i < len(diceList)):
            diceList[i] = GameRunner.isValidDice()
            i += 1
        if (GameRunner.AskRollDice(diceList, rolls) == 1):
            rolls += 1
        ValidateContinue()

Game()