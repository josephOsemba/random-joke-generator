import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why was the Python developer so calm? He had his 'try' block ready! 😎",
    "How do you comfort a JavaScript bug? You 'console' it. 🖥️",
    "Why did the developer go broke? Because he used up all his cache. 💸",
    "Why do Java developers wear glasses? Because they don't see sharp! 👓",
    "What is a programmer’s favorite hangout place? The 'foo' bar. 🍸",
    "Why did the Python programmer sneeze? He caught an exception! 🤧",
    "Why was the database sad? It had too many relationships to handle. 😢",
    "What do you call a group of 8 Hobbits? A Hobbyte. 🧙‍♂️",
    "Why did the computer cross the road? To fetch the data on the other side! 🚦"
]

random_joke = random.choice(jokes)

print("Random joke game")
print("-" * 30)
print(random_joke)
print("-" * 30)

list = [1, 2, 4, 8, 9, 8, 10, 3,5, 5, 6]

list.append(11)
list.extend([12, 13, 14, 15])
list.pop(8)
list.sort()

for number in list:
    print(number)


