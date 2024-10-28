def mul_even_odd(lst):
    evens, odds = [], []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0:
        return "No even number in the list"
    if len(odds) == 0:
        return "No odd number in the list"
    return evens[0] * odds[0]