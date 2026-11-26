while True:
    eded1 = input("Birinci rəqəmi daxil et: ")

    if eded1.isdigit():
        eded1 = int(eded1)
        break
    else:
        print("Rəqəm daxil et!")


while True:
    eded2 = input("İkinci rəqəmi daxil et: ")

    if eded2.isdigit():
        eded2 = int(eded2)
        break
    else:
        print("Rəqəm daxil et!")


while True:
    eded3 = input("Üçüncü rəqəmi daxil et: ")

    if eded3.isdigit():
        eded3 = int(eded3)
        break
    else:
        print("Rəqəm daxil et!")


list = [eded1, eded2, eded3]

sayi = 0
for cem in list:
    sayi = cem + sayi

if sayi > 20:
    print("Cəm böyükdür")
elif sayi < 20:
    print("Cəm kiçikdir")
elif sayi == 20:
    print("Müəllim qeyd etməyib ;)")
