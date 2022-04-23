#ebob-ekok bulma
def ebob_bulma(sayi1,sayi2):
    ebob = 1
    if sayi1 < sayi2:
        min = sayi1
        for i in range(1,min+1):
            if sayi1 % i == 0 and sayi2 % i == 0:
                ebob = i
        return ebob
    else:
        min = sayi2
        for i in range(1,min+1):
            if sayi1 % i == 0 and sayi2 % i == 0:
                ebob = i
        return ebob

sayi1=int(input("Lütfen ilk sayıyı giriniz: "))
sayi2=int(input("Lütfen ikinci sayıyı giriniz: "))

z = ebob_bulma(sayi1,sayi2)
print("Ebob: ",z)
print("Ekok: ",(sayi1*sayi2)/z)
