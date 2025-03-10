def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or more, it applies the discount; otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"Final Price: {final_price}")
