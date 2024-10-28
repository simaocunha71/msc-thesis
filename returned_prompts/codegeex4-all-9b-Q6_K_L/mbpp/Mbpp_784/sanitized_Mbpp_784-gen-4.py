def mul_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    if len(evens) >= 1 and len(odds) >= 1:
        return evens[0] * odds[0]
    else:
        return 0