def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (discount_percent/100)
        new_price = price - discounted_price
        return new_price
    else:
        return price

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)
print("Final price:", final_price)