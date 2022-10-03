#!/usr/bin/python3

import random as r
#paper = 0
#scissors = 1
#rock = 2
#lizard = 3
#spock = 4

loop = 1
userEntries = [0,0,0]
score = [0,0,0]

computer = ''
user = ''
cChoice = 0
uChoice = 0

game = 0

while loop == 1:
    #print the menu
    print('Menu')
    print('1: stats')
    print('2: exit')
    print('3: Paper Scissors Rock')
    print('4: Paper Scissors Rock Lizard Spock')
    #take users selection
    menu = input('please enter selection: ')

    if int(menu) == 1:
        #print statistics of the users session
        print("\n\n\n")
        print("You have won", score[0], "games")
        print("The computer has won", score[1], "games")
        print("There have been", score[2], "draws")
        print('\n')
        print("you have chosen paper", userEntries[0], "times")
        print("you have chosen scissors", userEntries[1], "times")
        print("you have chosen rock", userEntries[2], "times")
        print("\n\n\n")
    elif int(menu) == 2:
        #exit the game by breaking the loop
        loop = 0
    elif int(menu) == 3:
        game = 1
    elif int(menu) == 4:
        game = 2
        
    #Paper Scissors Rock
    if game == 1:
        print('\n\n\n')
        #select random for the computer
        cChoice = r.randint(0,3)
        #if computers choice is 3(wildcard, then use user statistics to select best option)
        if cChoice == 3:
            if userEntries[0] > userEntries[1]:
                if userEntries[0] > userEntries[2]:
                    cChoice = 1
                else:
                    cChoice = 0
            elif userEntries[1] > userEntries[2]:
                if userEntries[1] > userEntries[0]:
                    cChoice = 2
                else:
                    cChoice = 1
            else:
                if userEntries[2] > userEntries[1]:
                    cChoice = 0
                else:
                    cChoice = 2

        #convert computers choice to text
        if cChoice == 0:
            computer = 'paper'
        if cChoice == 1:
            computer = 'scissors'
        if cChoice == 2:
            computer = 'rock'

        #take users choice
        print("1: paper")
        print("2: scissors")
        print("3: rock")
        uChoice = input("please enter choice: ")
        uChoice = (int(uChoice) - 1)

        if uChoice == 0:
            user = 'paper'
            userEntries[0] += 1
        if uChoice == 1:
            user = 'scissors'
            userEntries[1] += 1
        if uChoice == 2:
            user = 'rock'
            userEntries[2] += 1

        print("You chose:", user)
        print("Computer chose:", computer, "\n")

        #calculate winner
        if uChoice == cChoice:
            print("Game Draw")
            score[2] += 1
        elif uChoice == 0:
            if cChoice == 1:
                print("Computer wins!")
                score[1] += 1
            else:
                print("You win!")
                score[0] += 1
        elif uChoice == 1:
            if cChoice == 2:
                print("Computer wins!")
                score[1] += 1
            else:
                print("You win!")
                score[0] += 1
        elif uChoice == 2:
            if cChoice == 0:
                print("Computer wins!")
                score[1] += 1
            else:
                print("You win!")
                score[0] += 1
        print('\n')
        #reset selection to show menu
        game = 0

    #Paper Scissors Rock Lizard Spock
    if game == 2:
        print('\n\n\n')
        #select random for computer
        cChoice = r.randint(0,4)
        
        if cChoice == 0:
            computer = 'paper'
        if cChoice == 1:
            computer = 'scissors'
        if cChoice == 2:
            computer = 'rock'
        if cChoice == 3:
            computer = 'lizard'
        if cChoice == 4:
            computer = 'spock'

        #take user input
        print("1: paper")
        print("2: scissors")
        print("3: rock")
        print("4: lizard")
        print("5: spock")
        uChoice = input("please enter choice: ")
        uChoice = (int(uChoice) - 1)

        if uChoice == 0:
            user = 'paper'
        if uChoice == 1:
            user = 'scissors'
        if uChoice == 2:
            user = 'rock'
        if uChoice == 3:
            user = 'lizard'
        if uChoice == 4:
            user = 'spock'

        print("You chose:", user)
        print("Computer chose:", computer, "\n")

        #calculate winner
        if uChoice == cChoice:
            print("Game Draw")
            score[2] += 1
        elif uChoice == 0:
            if cChoice == 1 or 3:
                print("Computer wins!")
            else:
                print("You win!")
        elif uChoice == 1:
            if cChoice == 2 or 4:
                print("Computer wins!")
            else:
                print("You win!")
        elif uChoice == 2:
            if cChoice == 0 or 4:
                print("Computer wins!")
            else:
                print("You win!")
        elif uChoice == 3:
            if cChoice == 1 or 2:
                print("Computer wins!")
            else:
                print("You win!")
        elif uChoice == 4:
            if cChoice == 0 or 3:
                print("Computer wins!")
            else:
                print("You win!")
        
        print('\n')
        #reset selection to show menu
        game = 0
    
