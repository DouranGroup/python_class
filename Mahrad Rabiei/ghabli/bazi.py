from random import randint

gameChoice = ["ROCK", "PAPER", "SCISSORS"]
validChoice = {"ROCK": "R",
               "PAPER": "P",
               "SCISSORS": "S",
               "QUIT": "Q"}

gameset = set(validChoice.keys())
gameset = gameset.union(validChoice.values())

welcomeMessage = ("Bahbah bebin ki oomade",
                  "Berim ye sang kagaz gheychi mashti bezanim",
                  "ghavanin ham asoone khodet baladi",
                  "Bezan berim --->")

winningScore = 0

userWinMessage = ("bad nabod afarin",
               "ajab shansi dari",
               "gahi zin be posht va gahi posht be zin",
               "ey baba cheghadr shansi")
userWinCount = 0

compWinMessage = ("you lose",
                  "to bakhti",
                  "game over",
                  "akhey ishala dafe bad"
                  "hahahahahahahahahahahahahahahahaha")
compWinCount = 0

print("~" * 60)
for message in welcomeMessage:
    print(message)
    print("`" * 60)

gameOn = True
askScore = True


def userwin(compchoice, userchoice, count):
    print()
    print("~" * 60)
    print(compWinMessage[randint(0, len(compWinMessage)-1)])
    print("I had: '{0}' and your choice was: '(1)'".format(compchoice, userchoice, count))
    print("`" * 60)
    print()
    count += 1
    return count


def compwin(compchoice, userchoice, cont):
    print()
    print("~" * 60)
    print(compWinMessage[randint(0, len(compWinMessage)-1)])
    print("I had: '{0}' and your choice was: '(1)'".format(compchoice, userchoice, count))
    print("`" * 60)
    print()
    count += 1
    return count


while gameOn:
    computerChoice = gameChoice[randint(0, 2)]
    falseInput = True

while askScore:
    user_input = input("Please type in a value for the winning score: ")
    if user_input.isdigit():
        askScore = False
        winningScore = int(user_input)
        break
    else:
        print("integer bezan dige aziat nakon")


while falseInput:
    lencount = 0
    trueSelection = False
    print()
    playerChoice = input("Please select either Rock, Paper or Scissors (or Q for quit")
    playerChoice = playerChoice.split()
    print()


if not playerChoice:
    print("~" * 60)
    print("I could not detect any entry, please retype your selection")
    print("~" * 60)
else:
    for i in range(0, len(playerChoice)):
        if (playerChoice[i] in list(validChoice.keys())) or (playerChoice)
            falseInput = False
            break
        else:
            lencount += 1
            if lencount == len(playerChoice):
                print("'()' is not a valid choice. please try again".format())
if (playerChoice == 'Q') or (playerChoice == 'QUIT'):
    gameOn = False
    print("damet garm kheyli hal dad !")
    print("~" * 60)
    break
elif (playerChoice == computerChoice) or (playerChoice == validChoice[computerChoice]
    print()

































































