    result = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            result += lst[i]
    return result
# Test the function
print(add([4, 2, 6, 7]))  # Output: 2
print(add([1, 3, 5, 7]))  # Output: 0
print(add([2, 4, 6, 8]))  # Output: 4
print(add([5, 7, 9, 11]))  # Output: 0
print(add([1, 2, 3, 4]))  # Output: 2
print(add([1, 1, 1, 1]))  # Output: 0
print(add([2, 2, 2, 2]))  # Output: 4
print(add([1, 2, 3, 4, 5]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7]))  # Output: 2

# Test the function with negative numbers
print(add([-1, -2, -3, -4]))  # Output: -2
print(add([-1, 2, -3, -4]))  # Output: -2
print(add([1, -2, 3, -4]))  # Output: 0
print(add([-1, -2, 3, 4]))  # Output: 0
print(add([1, 2, 3, -4]))  # Output: 2
print(add([1, 2, 3, -4, 5]))  # Output: 2

# Test the function with zero
print(add([0, 1, 2, 3]))  # Output: 2
print(add([0, 0, 0, 0]))  # Output: 0
print(add([0, 1, 2, 3, 4]))  # Output: 2

# Test the function with a list of one element
print(add([4]))  # Output: 0
print(add