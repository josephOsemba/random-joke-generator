#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

set1 = set()

set2 = set()

message = "Enter number of elements for set1 (maximum is 5): "
print(message)
n = 1
while n<=5:
    element = int(input("Enter element: "))
    set1.add(element)
    n += 1

message = "Enter number of elements for set2 (maximum is 5): "
print(message)

n = 5

for i in range(n):
    element = int(input("Enter element: "))
    set2.add(element)

common_elements = set1.intersection(set2)
print("Common elements: ", common_elements)

