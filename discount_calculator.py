def calculate_discount(price, discount_percentage):
#If statement to check the discount against 20% and whether it should discount the price or not
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage/100)
        discounted_price = round(price - discount_amount, 2)
        return  discounted_price
    else:
        return price
#The variables take the users inputs to work in the function    
product_price = float(input('How much does the product cost? '))
percent = float(input('what is the discount percentage(omit %)? '))
#Calling the function
pricing = calculate_discount(product_price,percent)
print('this is the price: ', pricing)