#Create a function named calculate_discount(price, discount_percent) that calculates the 
# final price after applying a discount. The function should take the original price (price) 
# and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.


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