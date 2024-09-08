def first_odd(lst):
    for number in lst:
        if number % 2 == 1:
            return number
    return None