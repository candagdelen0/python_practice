def slash(num):
    for i in range(int(num)):
        print("/",end="")

def reverseSlash(num):
    for i in range(int(num)):
        print("\\",end="")

def spaces(num):
    for i in range(int(num)):
        print(" ",end="")

def jump(num):
    for i in range(int(num)):
        print()

def parallelogram(number):
    for i in range(int(number/2)):
        spaces((number/2-1)-i)
        slash(1)
        spaces(i*2)
        reverseSlash(1)
        jump(1)
    for i in range(int(number/2-1),-1,-1):
        spaces(number/2-i-1)
        reverseSlash(1)
        spaces(i*2)
        slash(1)
        jump(1)

parallelogram(10)
