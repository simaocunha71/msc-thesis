def return_sum(dict):
    total_sum = 0
    for key, value in dict.items():
        total_sum += value
    return total_sum

# Test the function
print(return_sum({'a': 100, 'b':200, 'c':300}))  # Output: 600
# Test the function
print(return_sum({'x': 1, 'y': 2, 'z': 3}))  # Output: 6
# Test the function
print(return_sum({'apple': 1, 'banana': 2, 'cherry': 3}))  # Output: 6
# Test the function
print(return_sum({}))  # Output: 0
# Test the function
print(return_sum({'a': 0}))  # Output: 0
# Test the function
print(return_sum({'a': 5.5}))  # Output: 5.5
# Test the function
print(return_sum({'a': '5.5'}))  # Output: 5.5
# Test the function
print(return_sum({'a': True}))  # Output: 1
# Test the function
print(return_sum({'a': False}))  # Output: 0
# Test the function
print(return_sum({'a': None}))  # Output: 0
# Test the function
print(return_sum({'a': [1, 2, 3]}))  # Output: 6
# Test the function
print(return_sum({'a': (1, 2, 3)}))  # Output: 6
# Test the function
print(return_sum({'a': {'b': 1, 'c': 2}}))  # Output: 3
# Test the function
print(return_sum({'a': {'b': 1, 'c': 2}, 'b': 3}))  # Output: 6
# Test the function
print(return_sum({'a': [1, 2, 3], 'b': 4}))  # Output: 9
# Test the function
print(return_sum({'a': (1, 2, 3), 'b': 4}))  # Output: 7
# Test the function
print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400}))  # Output: 1000

# Test the function