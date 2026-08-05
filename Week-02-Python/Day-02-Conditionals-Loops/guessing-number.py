# guessing numbers
number = 7
guess = 0
while guess != number:
 guess = int(input("enter the num(1-10): "))
 if guess > number:
           print("too high")
 elif guess < number:
    print("too low")
 else:
    print("Congratulations!You Geussed The Correct One")         

