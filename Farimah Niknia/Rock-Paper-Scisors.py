import random
import sys
from typing import List

validation = bool
computerScore = 0
userScore = 0
playAgain = 'yes'
print('Welcome to My Game\n'
      'Here You Have a Chance to Play the Game of Rock-Paper-Scissors With Me\n'
      'Rules Are Simple: \n'
      'Rock Smashes Scissors\n'
      'Scissors Cut Paper\n'
      'Paper Covers Rock\n'
      'Hope You Enjoy It !')
print('*' * 80)
choices = ['Rock', 'Paper', 'Scissors']
while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
    while True:
        userInput = input('Please Type in a Value for the Wining Score:\n')
        if userInput.isdigit():
            winingScore = int(userInput)
            break
        else:
            print('I need an integer to carry on.\n')
    while validation:
        comChoice = (random.choice(choices))
        print('=' * 80)
        userChoice = input('Please select either Rock, Paper or Scissors or QUIT to exit:\n')
        userChoice = userChoice.split()
        for word in userChoice:
            if word.lower() == 'rock' or word.lower() == 'r':
                print('Your choice was Rock and I had', comChoice)
                if comChoice == 'Rock':
                    print(' Computer Score: ', computerScore, '\n User Score: ', userScore)
                elif comChoice == 'Paper':
                    computerScore = computerScore + 1
                    print(' Computer Score:', computerScore, '\n User Score:', userScore)
                elif comChoice == 'Scissors':
                    userScore = userScore + 1
                    print(' Computer Score:', computerScore, '\n User Score:', userScore)
                if userScore - computerScore == winingScore or computerScore - userScore == winingScore:
                    validation = False
                break
            elif word.lower() == 'paper' or word.lower() == 'p':
                print('your choice was Paper and I had', comChoice)
                if comChoice == 'Rock':
                    userScore = userScore + 1
                    print(' Computer Score:', computerScore, '\n User Score:', userScore)
                elif comChoice == 'Paper':
                    computerScore = computerScore + 1
                    print(' Computer Score', computerScore, '\n User Score:', userScore)
                elif comChoice == 'Scissors':
                    computerScore = computerScore + 1
                    print(' Computer Score:', computerScore, '\n User Score:', userScore)
                if userScore - computerScore == winingScore or computerScore - userScore == winingScore:
                    validation = False
                break
            elif word.lower() == 'scissor' or word.lower() == 's':
                print('your choice was Scissors and I had', comChoice)
                if comChoice == 'Rock':
                    computerScore = computerScore + 1
                    print(' Computer Score:', computerScore, '\n User Score:', userScore)
                elif comChoice == 'Paper':
                    userScore = userScore + 1
                    print(' Computer score', computerScore, '\n User Score:', userScore)
                elif comChoice == 'Scissors':
                    print(' Computer score:', computerScore, '\n User Score:', userScore)
                if userScore - computerScore == winingScore or computerScore - userScore == winingScore:
                    validation = False
                    break
            elif word.lower() == 'quit' or word.lower() == 'q':
                sys.exit()
    playAgain = input('Do you want to play again? (yes/no)')
    if playAgain.lower() == 'yes' or playAgain.lower() == 'y':
        validation = True
        computerScore = 0
        userScore = 0
    else:
        print('it was fun. I hope to see you soon')

