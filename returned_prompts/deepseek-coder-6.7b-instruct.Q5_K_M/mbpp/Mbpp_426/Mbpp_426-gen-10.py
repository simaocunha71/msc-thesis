def filter_perfect_squares(lst):
    return [i for i in lst if i**0.5==int(i**0.5)]

print(filter_perfect_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Write a function to filter numbers which are palindromes.
assert filter_