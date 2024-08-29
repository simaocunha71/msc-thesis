
def is_product_even(lst):
    product = 1
    for i in lst:
        product *= i
    return product % 2 == 0

assert is_product_even([1,2,3]) == False

#Task 4:

