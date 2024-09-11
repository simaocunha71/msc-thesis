def mul_even_odd(l):
    odd_list = []
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if len(odd_list) == 0:
        return 0
    if len(even_list) == 0:
        return 0
    else:
        return odd_list[0] * even_list[0]