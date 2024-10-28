    array_copy = array.copy()
    sum_first_last = array_copy[0] + array_copy[-1]
    if sum_first_last % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy
    # You can also use sorted() function and list comprehension
    # return sorted(array_copy, reverse=(sum_first_last % 2 == 0))  # Python >= 3.0


