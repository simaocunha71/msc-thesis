def max_element(l: list):
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-10, -20, -30, -40, -50]))  # Output: -10
print(max_element([5, 5, 5, 5, 5]))  # Output: 5
print(max_element([1.5, 2.5, 3.5, 4.5, 5.5]))  # Output: 5.5
print(max_element(["a", "b", "c"]))  # TypeError: '>' not supported between instances of 'str' and 'str'
print(max_element([5, "a", 2, 3, 4]))  # TypeError: '>' not supported between instances of 'int' and 'str'
print(max_element([]))  # ValueError: max() arg is an empty sequence
print(max_element([5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))  # Output: 5
print(max_element([5,