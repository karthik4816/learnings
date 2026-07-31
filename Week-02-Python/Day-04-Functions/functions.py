#Defining a Function
def hello():
    print("Hello, Karthik!")

hello()

#Function with Parameters
def greet(name):
    print("Hello", name)

greet("Karthik")
greet("Thomas")

#Return Statement
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

#Local Variables
def demo():
    x = 10
    print(x)

demo()

#Global Variables
name = "Karthik"

def display():
    print(name)

display()

#Built-in Functions
print("Hello")

print(len("Python"))

print(type(10))

print(max(2, 8))

#User-defined Functions
def greet():
    print("Welcome")

greet()