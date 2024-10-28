def unique_product(my_list):
    s = set()
    for x in my_list:
        if x not in s:
            s.add(x)
    return 1 if len(s) == 0 else 1 * reduce(lambda x, y: x * y, s)
