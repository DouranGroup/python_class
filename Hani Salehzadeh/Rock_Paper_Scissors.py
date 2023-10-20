import random
k = 0
endOfGame = 0
lucky = '\n' + '=' * 40 + '\nmy heavens, how could you be so in luck.'
unlucky = '\n' + '=' * 40 + '\nhahaaa, in your face !'
equal = '\n' + '=' * 40 + "\nit's a tie! seems our choices are the same."
computerChoices = 'paper', 'rock', 'scissors'
print('*' * 40)
print('Welcome to my game.')
print('Here you have a chance to play the game of Rock_Paper_Scissors with me.')
print('Rules are simple:')
print('\tRock smashes scissors.\n\tScissors cut paper.\n\tPaper covers rock.\nHope you enjoy it !')
print('*' * 40)
while True:
    while True:
        value = input('\nplease type in a value for the winning score:')
        for firstChar in value:
            if firstChar in '0123456789':
                continue
            else:
                print('\n(I need an integer to carry on. please type in an integer value)')
                break
        else:
            break
    if int(value) == 0:
        print('\n(please enter a value greater than 0)')
        continue
    print('\n')
    myScore = 0
    computerScore = 0
    word = ''
    while True:
        computerChoice = random.choice(computerChoices)
        myChoice = input('*' * 40 + '\nplease select either Rock, paper or scissors (or QUIT to exit):')
        words = myChoice.split()
        for word in words:
            if word.lower() in ['s', 'scissors']:
                if computerChoice == 'paper':
                    print(lucky)
                    print(f'I had paper and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    myScore += 1
                if computerChoice == 'rock':
                    print(unlucky)
                    print(f'I had rock and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    computerScore += 1
                if computerChoice == 'scissors':
                    print(equal)
                    print(f'I had scissors and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                break
            elif word.lower() in ['p', 'paper']:
                if computerChoice == 'paper':
                    print(equal)
                    print(f'I had paper and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                if computerChoice == 'rock':
                    print(lucky)
                    print(f'I had rock and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    myScore += 1
                if computerChoice == 'scissors':
                    print(unlucky)
                    print(f'I had scissors and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    computerScore += 1
                break
            elif word.lower() in ['r', 'rock']:
                if computerChoice == 'paper':
                    print(unlucky)
                    print(f'I had paper and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    computerScore += 1
                if computerChoice == 'rock':
                    print(equal)
                    print(f'I had rock and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                if computerChoice == 'scissors':
                    print(lucky)
                    print(f'I had scissors and your choice was {word.lower()}\n' + '=' * 40 + '\n')
                    myScore += 1
                break
            elif word.lower() in ['q', 'quit']:
                endOfGame = 1
                break
            else:
                continue
        else:
            print(f'\n({repr(myChoice)} is not a valid choice. please try again)\n')
            continue
        if endOfGame == 1:
            break
        print(('.' * 40) + '\n' + f'computer score is : {computerScore}\nyour score is : {myScore}'
              + '\n' + ('.' * 40) + '\n')
        if (myScore == int(value)) | (computerScore == int(value)):
            break
    if endOfGame == 1:
        break
    print('*' * 40)
    if myScore == int(value):
        print('well done, you have won the game\n')
    else:
        print('WoooHooo, I have won the game\n')
    print('*' * 40)
    while True:
        nextRound = input('care to play another round? [yes/no]\n')
        words = nextRound.split()
        for word in words:
            if word.lower() in ['y', 'yes']:
                print("\nAlright, Let's do one more\n")
                break
            elif word.lower() in ['n', 'no']:
                endOfGame = 1
                break
            else:
                continue
        else:
            print("\n(you need to tell me exactly what to do. I need a 'yes' or 'no')\n")
            continue
        break
    if endOfGame == 1:
        break
print('\nThank you for playing this game. GOODBYE')
