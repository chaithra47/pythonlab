#function

#Defining a function
def greet():
    print("Hello")

greet() # Function call

#Function with parameters
def greet(name):
    print("Hello, {name}")

greet("Alice") 
#Function with a return value
def add(a, b)->int:
    return a + b # result v ar here is a diffrent variable declared in local scope
    return result
#------------------------------------------------------------------------------
result = add(5.5,4) #result variable is another diffrent var, which is with the scope outside the function defination
print(result) 

#Default parameter values

def greet(name = "Guest"):
    print("Hello, {name}")

greet()
greet("Bob")

#Arbitrary arguments

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1,2,3,4,5))

#keyword arguments(**kwargs)

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice",age=25,city="NYC")

#Lamba function-> short,inline function

square = lambda x: x**2
print(square(5))

#recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def add(a:int,b:int)->int:
    result = int(a)+int(b)#Explict conversion
    return result
#------------------------------------------------------------------------------------------
result = add(5.5,4.5) #able to get the integer result
print(result)  