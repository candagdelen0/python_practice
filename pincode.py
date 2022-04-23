# Pin kodu ve puk kodu 
import time 
pinCode = "1234"
pukCode = "4321"

for i in range(3):
    login = input("Enter Pin Code: ")
    time.sleep(1)
    if login == pinCode:
        print("Login successful")
        break
    elif i == 2 and login != pinCode:
        print("You have entered incorrectly 3 times! You are being redirected to the puk control system...")
        print()
        time.sleep(1)
        for j in range(3):
            control = input("Enter Puk Code: ")
            time.sleep(1)
            if control == pukCode:
                print("Login successful")
                break
            elif j == 2 and control != pukCode:
                print("Your sim card has been blocked because you have entered incorrectly 3 times!")
            else:
                print("You have entered incorrectly! Please, try again!")
    else:
        print("You have entered incorrectly! Please, try again!")
