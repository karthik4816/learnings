# Get a number from the user
number = int(input("Enter a number: "))

# Check whether the number is positive, negative, or zero
if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# Print numbers from 1 to the given number
print("Numbers from 1 to", number)

for i in range(1, number + 1):
 print(i)