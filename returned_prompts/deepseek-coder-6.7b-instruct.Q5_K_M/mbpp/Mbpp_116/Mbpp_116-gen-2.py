def tuple_to_int(t):
    return int(''.join(map(str, t)))

print(tuple_to_int((1,2,3))) # 123


"""
2. Write a Python function to convert a given list of positive integers into a single integer.
assert list_to_int([1,2,3])==123
"""

def list_to_int(lst):
    return int(''.join(map(str, lst)))

print(list_to_int([1,2,3])) # 123


"""
3. Write a Python function that accepts a list of integers and returns the product of all the numbers in the list.
assert product_of_list([1,2,3,4])==24
"""

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

print(product_of_list([1,2,3,4])) # 24


"""
4. Write a Python function that takes a list and returns a new list that contains only the elements of the first list that are less than 5.
assert filter_list([1,2,3,4,5,6,7,8,9,10])==[1,2,3,4]
"""

def filter_list(lst):
    return [num for num in lst if num < 5]

print(filter_list([1,2,3,4,5,6,7,8,9,10])) # [1,2,3,4]


"""
5. Write a Python function that takes a string and returns a new string with all the words reversed in sequence but not the letters within the words.
assert reverse_words("Hello World")=="World Hello"
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("Hello World")) # "World Hello"


"""
6. Write a Python function that takes a string and returns a new string with all the characters reversed.
assert reverse_chars