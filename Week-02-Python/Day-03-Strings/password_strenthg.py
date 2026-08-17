password = input("enter password: ")

# as_upper = False
# has_lower = False
# has_digit = False
# has_special = False

special_chars = "@#$%&!"
print("length",len(password))

for ch in password:

    if ch.isupper():
        has_upper = True
        print("has upeer",has_upper) 
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
        

if len(password) < 8:
    print("weak password")

elif has_upper and has_lower  and has_digit and has_special:
         print("strong password")
elif has_upper and has_lower:
        print("weak password")
else:
      print('weak password')          