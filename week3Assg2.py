# Using the calculate_discount function, prompt the user to enter 
# the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if 
#no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    price = int(input("Enter price: "))
    discount_percent = int(input("Enter discount percent(out of 100%): "))

    discount = price * discount_percent / 100

    final_price = price - discount

    if discount_percent > 100 or discount_percent < 0:
        return f"Invalid discount percent. Please try again."
    elif discount_percent < 20:
        return f"Selling price is: {price}"
    else:
        return f"Selling price is: {final_price}"
    


print(calculate_discount( price=100, discount_percent=20))