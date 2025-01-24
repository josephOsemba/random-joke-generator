#Write a program that uses a dictionary to store information about a person, 
#such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. 
#Then, print the dictionary to the console.

person = {}

print(type(person))

name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")

person["name"] = name
person["age"] = age
person["color"] = color

print(f"-" * 30)
for i in person:
    print(i + ": " + person[i])
print("-" * 30)