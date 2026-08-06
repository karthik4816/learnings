num = 7
geuss = 0
while geuss != num:
    geuss = int(input("enter: "))

    if geuss > num:
        print('high')
    elif geuss < num:
        print("low")
    else:
        print("correct")        