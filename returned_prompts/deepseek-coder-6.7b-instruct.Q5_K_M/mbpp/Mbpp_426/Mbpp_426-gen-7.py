def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 == 0]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # should return [2, 4, 6, 8, 10]

"""
