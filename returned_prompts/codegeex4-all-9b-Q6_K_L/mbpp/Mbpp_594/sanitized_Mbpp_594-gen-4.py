def diff_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    if evens and odds:
        return evens[0] - odds[0]
    else:
        return "No even or odd number found in the list"