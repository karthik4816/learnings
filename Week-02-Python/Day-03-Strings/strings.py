#strings
name = "karthik" # A string is an character enclosed in qoutes
color = 'blue is the color'
city = "  lives in hyd  "
print(name)
print(color)

#string indexing
print(name[0])
print(name[4])
print(name[-1])
print(name[-3])

#string slicing
print(name[2:4])
print(name[:4])
print(name[3:])
print(name[::5])
print(name[:])

#string length
print(len(name))

#Common String Methods
print(name.upper())
print(name.lower())
print(color.title())
print(city.strip())
print(name.replace("karthik","jhon"))
print(color.split())
print(name.find("h"))
print(name.count("k"))

#String Operators
print(name + "" + city)
print(name * 3)

#Membership
print("ka" in name)
print("eya" in name)
 
#f-Strings
print(f"welcome {name} who {city}")

