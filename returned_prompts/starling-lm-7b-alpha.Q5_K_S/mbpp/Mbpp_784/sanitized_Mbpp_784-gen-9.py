def mul_even_odd(lst):
    evens = [i for i in lst if i % 2 == 0]
    odds = [i for i in lst if i % 2 != 0]
    if len(evens) > 0:
        even = evens[0]
    else:
        even = 0
    if len(odds) > 0:
        odd = odds[0]
    else:
        odd = 0
    return even * odd