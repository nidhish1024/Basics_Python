<<<<<<< HEAD
def apply_discount(price,discount):

    if not(isinstance(price,int) or isinstance(price,float)):
        return'The price should be a number'

    if price<=0:
        return'The price should be greater than 0'


    if not(isinstance(discount,int) or isinstance(discount,float)):
        return'The discount should be a number'

    if discount<0 or discount>100:
        return'The discount should be between 0 and 100'

    final_result=price-price*discount/100
    return final_result

def  type_check(value):
    if (isinstance(value,int) or isinstance(value,float)):
        return True
    else:
        return False

    
price=int(input('Enter the price:'))
discount=int(input('Enter the discount:'))

if type_check(price):
    print('Invalid price entered.')
elif type_check(discount):
    print('Invalid discount entered.')
else:
    result=apply_discount(price,discount)
    print('Price after applying discount:',result)
=======
def apply_discount(price,discount):

    if not(isinstance(price,int) or isinstance(price,float)):
        return'The price should be a number'

    if price<=0:
        return'The price should be greater than 0'


    if not(isinstance(discount,int) or isinstance(discount,float)):
        return'The discount should be a number'

    if discount<0 or discount>100:
        return'The discount should be between 0 and 100'

    final_price=price-price*discount/100
    return final_price

price=int(input('Enter the price:'))
discount=int(input('Enter the discount:'))
price_after_discount=apply_discount(price,discount)
print('Output:',price_after_discount)
    
>>>>>>> 208c3b19360484479888da83fcae84d4564eb5a1
