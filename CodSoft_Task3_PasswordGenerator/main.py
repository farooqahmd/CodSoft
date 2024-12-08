import random

uppercase_letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits ="0123456789"
symbols ="(){}[],;:.?!@#$%^&*"

upper,lower,nums,syms = True,True,True,True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

while True:
    length = int(input("Enter the length of the password ( Should be atleast 8 characters): "))
    if length >= 8 :
        break

amount = int(input("Enter the amount of the passwords you want to generate: "))

for x in range(amount):
    password ="".join(random.sample(all,length))
    print(password)