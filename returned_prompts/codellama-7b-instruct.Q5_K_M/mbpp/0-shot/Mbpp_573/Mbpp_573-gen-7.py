def unique_product(my_list):
    s = set()
    result = 1
    for i in my_list:
        if i not in s:
            s.add(i)
            result *= i
    return result

