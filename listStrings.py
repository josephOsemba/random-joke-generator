#Create a program that stores a list of words. Then, use list comprehension 
# to create a new list that contains only the words that have an odd number of characters.

words = ["apple", "banana", "orange", "mango", "kiwi", "pear", "grape", "strawberry", "blueberry", "raspberry"]

odd_words = [word for word in words if len(word) % 2 != 0]

print(odd_words)