def first_odd(lst):
    for i in lst:
        if i % 2 != 0:
            return i
    return None  # return None if no odd number is found