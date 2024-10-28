def mul_even_odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        return 0
    if len(even) == 0:
        return odd[0]
    return even[0] * odd[0]