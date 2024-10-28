def mul_even_odd(lst):
    evens = []
    odds = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0 or len(odds) == 0:
        return None
    else:
        return evens[0] * odds[0]