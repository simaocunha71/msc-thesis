
def is_product_even(my_list):
    result = True
    for num in my_list:
        if num % 2 != 0:
            result = False
            break
    return result


