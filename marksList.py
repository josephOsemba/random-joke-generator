#Write a program that accepts user input to create a list of integers. 
#Then, compute the sum of all the integers in the list.
#The program should stop accepting input when the user enters "q" to quit.

marks = []

while True:
    mark = input("Enter a mark or q to sum: ")
    if mark == "q":
        mark_sum = sum(marks)
        print("Sum of marks is: " + str(mark_sum))
        break
    marks.append(int(mark))