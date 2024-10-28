def nth_nums(lst, n):
    return [x**n for x in lst]  # or use map: return list(map(lambda x: x**n, lst))  # or use list comprehension with if condition