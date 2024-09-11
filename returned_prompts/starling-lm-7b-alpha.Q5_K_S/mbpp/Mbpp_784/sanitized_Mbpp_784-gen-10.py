def mul_even_odd(num_list):
    even, odd = [], []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0:
        return 0
    elif len(odd) == 0:
        return even[0]
    else:
        return even[0] * odd[0]