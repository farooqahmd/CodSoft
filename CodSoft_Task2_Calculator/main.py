def addition(a, b):
     return a+b

def subtraction(a, b):
     return a-b

def multiplication(a, b):
     return a*b

def division(a, b):
     return a/b

def remainder(a, b):
     return a%b

ask =int(input('What do you want to perform?\n1.Addition\n2.Subtraction\n3.Multiplication/n4.Division\n5.Remainder\n'))

if ask==1:
     num1 =int(input("Enter the first number: "))
     num2 =int(input("Enter the second number: "))
     print(addition(num1,num2))

elif ask==2:
     num1 =int(input("Enter the first number: "))
     num2 =int(input("Enter the second number: "))
     print(subtraction(num1,num2))

elif ask==3:
     num1 =int(input("Enter the first number: "))
     num2 =int(input("Enter the second number: "))
     print(multiplication(num1,num2))

elif ask==4:
     num1 =int(input("Enter the first number: "))
     num2 =int(input("Enter the second number: "))
     print(division(num1,num2))

elif ask==5:
     num1 =int(input("Enter the first number: "))
     num2 =int(input("Enter the second number: "))
     print(remainder(num1,num2))

