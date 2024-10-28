"""
def mul_even_odd(my_list):
    # initialize variables
    product_even = 1
    product_odd = 1
    # iterate over the list
    for i in my_list:
        # if the number is even multiply by 2
        if i % 2 == 0:
            product_even *= i
        # if the number is odd multiply by 2
        else:
            product_odd *= i
    # return the product of even and odd numbers
    return product_even * product_odd
"""