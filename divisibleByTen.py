

def divisible_by_ten(num):
    """
    Create a function called divisible_by_ten() that has one parameter named num.
    The function should return True if num is 
    divisible by 10, and False otherwise. Consider using modulo 
    operator % to check for divisibility.
    """
    number = num
    number = int(input("Enter a number: "))
    if number % 10 == 0:
        print(f"{number} is divisible by 10")
    else:
        print(f"{number} is not divisible by 10")

divisible_by_ten(10)