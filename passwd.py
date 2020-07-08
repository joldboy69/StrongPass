#made by joldboy69. DO NOT STEAL MY SCRIPT.

import random
import string

lol = string.ascii_letters + string.digits + string.punctuation

maxLength = int(input("Enter the max length of each password: "))
minLength = int(input("Enter the minimum length for each password: "))
times = int(input("Enter the amount of passwords to generate: "))

password = ""

for c in range(times):
    for i in range(random.randint(minLength, maxLength)):
        password += random.choice(lol)
    print(password)
    password = ""
