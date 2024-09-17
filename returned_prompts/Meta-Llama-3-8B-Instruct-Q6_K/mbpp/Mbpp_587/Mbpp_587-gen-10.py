def list_tuple(lst):
    return tuple(lst)
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
print(list_tuple([5, 10, 7, 4, 15, 3])) # Output: (5, 10, 7, 4, 15, 3)  # Test case 1
print(list_tuple(['a', 'b', 'c'])) # Output: ('a', 'b', 'c')  # Test case 2
print(list_tuple([1.5, 2.5, 3.5, 4.5, 5.5])) # Output: (1.5, 2.5, 3.5, 4.5, 5.5)  # Test case 3
print(list_tuple([True, False, True])) # Output: (True, False, True)  # Test case 4
print(list_tuple(['hello', 'world'])) # Output: ('hello', 'world')  # Test case 5
print(list_tuple([1, 2, 3, 4, 5])) # Output: (1, 2, 3, 4, 5)  # Test case 6
print(list_tuple([5, 10, 7, 4, 15, 3])) # Output: (5, 10, 7, 4, 15, 3)  # Test case 7
print(list_tuple(['a', 2, 3.5, True, 'hello'])) # Output: ('a', 2, 3.5, True, 'hello')  # Test case 8
print(list_tuple(['a', 'b', 'c', 'd', 'e', 'f'])) # Output: ('a', 'b', 'c', 'd', 'e', 'f')  # Test case 9
print(list_tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Test case 10
print(list_tuple([10, 20,