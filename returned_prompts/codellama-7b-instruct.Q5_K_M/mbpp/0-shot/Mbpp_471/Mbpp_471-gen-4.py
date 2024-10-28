def find_remainder(my_list,modulo):
    product = 1
    for i in my_list:
        product *= i
        product %= modulo
    return product
