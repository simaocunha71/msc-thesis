def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]

assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1,3,5,7,9]
print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: [1, 3, 5, 7, 9]  # Test case 1

print(filter_oddnumbers([2, 2, 2, 2, 2])) # Output: []  # Test case 2

print(filter_oddnumbers([1, 1, 1, 1, 1])) # Output: [1, 1, 1, 1, 1]  # Test case 3

print(filter_oddnumbers([])) # Output: []  # Test case 4

print(filter_oddnumbers([10])) # Output: []  # Test case 5

print(filter_oddnumbers([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Output: [11, 13, 15, 17, 19]  # Test case 6

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Test case 7

print(filter_oddnumbers([1, 1, 1, 1, 1, 1])) # Output: [1, 1, 1, 1, 1, 1]  # Test case 8

print(filter_oddnumbers([2, 2, 2, 2, 2, 2])) # Output: []  # Test case 9

print(filter_oddnumbers([1, 1, 1, 1, 1, 1, 1, 1, 