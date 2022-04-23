import random
scoreUser = 0
scoreMachine = 0
counter = 0
gameList = ["Rock","Paper","Scissors"]
print("Welcome to Rock-Paper-Scissors Game!")
print()
userName = input("User Name: ")
for i in range(50):
    userChoice = input("(R)ock\n(P)aper\n(S)cissors\nYour choice: ")
    machineChoice = random.choice(gameList)
    print()
    if userChoice == "R" or userChoice == "r":
        print("{} choice: Rock and Computer's choice: {}".format(userName,machineChoice))
        if machineChoice == "Paper":
            scoreMachine += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        elif machineChoice == "Scissors":
            scoreUser += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        else:
            print("Same choice!\n")
            counter += 1
    elif userChoice == "P" or userChoice == "p":
        print("{} choice: Paper and Computer's choice: {}".format(userName,machineChoice))
        if machineChoice == "Rock":
            scoreUser += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        elif machineChoice == "Scissors":
            scoreMachine += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        else:
            print("Same choice!\n")
            counter += 1
    elif userChoice == "S" or userChoice == "s":
        print("{} choice: Scissors and Computer's choice: {}".format(userName,machineChoice))
        if machineChoice == "Rock":
            scoreMachine += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        elif machineChoice == "Paper":
            scoreUser += 2
            print(f"{userName}: {scoreUser}   Computer: {scoreMachine}\n")
        else:
            print("Same choice!\n")
            counter += 1
    else:
        print("You have entered incorrectly a choice, please try again...\n")

    if scoreMachine == 10:
        print("  The winner: COMPUTER  ".center(50,"*"))
        print(f"The number of games {userName} won: {int(scoreUser/2)}, the number of games computer won: {int(scoreMachine/2)}")
        print(f"The number of tied games is: {counter}")
        break
    elif scoreUser == 10:
        print(f"  The winner: {userName}  ".center(50,"*"))
        print(f"The number of games {userName} won: {int(scoreUser/2)}, the number of games computer won: {int(scoreMachine/2)}")
        print(f"The number of tied games is: {counter}")
        break

