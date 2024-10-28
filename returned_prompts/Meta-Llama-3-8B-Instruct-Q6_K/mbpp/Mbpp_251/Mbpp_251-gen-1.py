def insert_element(lst, element):
    return [element] + lst + [element]

# Test the function
print(insert_element(['Red', 'Green', 'Black'], 'c'))  # Expected output: ['c', 'Red', 'c', 'Green', 'c', 'Black']
print(insert_element([1, 2, 3], 'a'))  # Expected output: ['a', 1, 'a', 2, 'a', 3]
print(insert_element([1, 2, 3], 4))  # Expected output: [4, 1, 4, 2, 4, 3]  # Note that the element is inserted as is, not converted to a string. 
print(insert_element(['a', 'b', 'c'], 1))  # Expected output: [1, 'a', 1, 'b', 1, 'c']
print(insert_element(['a', 'b', 'c'], 'd'))  # Expected output: ['d', 'a', 'd', 'b', 'd', 'c'] 
print(insert_element([1, 2, 3], None))  # Expected output: [None, 1, None, 2, None, 3]  # Note that the element is inserted as is, not converted to a string. 
print(insert_element([1, 2, 3], True))  # Expected output: [True, 1, True, 2, True, 3]  # Note that the element is inserted as is, not converted to a string.  # 
print(insert_element(['a', 'b', 'c'], 'd'))  # Expected output: ['d', 'a', 'd', 'b', 'd', 'c'] 
print(insert_element([1, 2, 3], 'a'))  # Expected output: ['a', 1, 'a', 2, 'a', 3] 
print(insert_element([], 'a'))  # Expected output: ['a'] 
print(insert_element([], None))  # Expected output: [None] 
print(insert_element([], True))  # Expected output: [True] 
print(insert_element([], 'a'))  # Expected output: ['a'] 
print(insert_element([], None))  # Expected output: [None] 
print(insert_element([], True))  # Expected output: [True] 
print(insert