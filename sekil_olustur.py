import time
userName = input("User Name: ")
print(f"Hello {userName}!")
numb = int(input("How many times do you want to play: "))

for i in range(0,numb):
    model = input(f"1- Right Triangle\n2- Equilateral triangle\n3- Square\n4- Rectangle\nEnter another value to exit\nWhich shape would you like to choose {userName}: ")
    print()
    if model == "1":
        row = int(input("How many rows should this right triangle be drawn: "))
        for a in range(1,row+1):
            print("*"*a)
            print()
    elif model == "2":
        row = int(input("How many rows should this equilateral triangle be drawn:  "))
        for b in range(1,row+1):
            print(" "*(row-b) + "*"*(b*2-1))
            print()
    elif model == "3":
        row = int(input("How many rows should this square be drawn:  "))
        for c in range(1,row+1):
            print("* "*row)
            print()
    elif model == "4":
        row = int(input("How many rows should this rectangle be drawn: : "))
        column = int(input("How many columns should this rectangle be drawn: : "))
        for d in range(1,row+1):
            print("* "*column)
            print()
    else:
        print("The game is ending...")
        time.sleep(1)
