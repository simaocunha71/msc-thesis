    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
# This function works by iterating over the list with enumerate, which returns the index and value of each element. It checks if the index is a multiple of 3 or 4, and if it is, it squares or cubes the value and adds it to the total. If the index is not a multiple of 3 or 4, it simply skips it. At the end, it returns the total.