def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]  # filter out odd numbers
    # or return [i for i in lst if not i % 2]  # same result, different syntax