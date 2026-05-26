email = "bruce.wayne@batman.com"
parts = email.split("@")
print (parts)
print(parts[1])

num = input("Input a number: ")
try:
    num = int(num)

except ValueError:
    print("Enter a valid number")

import os
print(os.listdir("."))

with open("dummy.txt","w") as file:
    file.write("Hello World")

os.rename("dummy.txt", "important_data.txt")