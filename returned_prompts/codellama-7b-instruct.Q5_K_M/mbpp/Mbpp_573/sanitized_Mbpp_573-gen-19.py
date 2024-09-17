def unique_product(my_list):
    unique = set()
    result = 1
    for i in my_list:
        if i not in unique:
            unique.add(i)
            result *= i
    return result