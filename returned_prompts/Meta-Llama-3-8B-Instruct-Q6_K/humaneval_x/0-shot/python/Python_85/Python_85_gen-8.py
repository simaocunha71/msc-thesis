    result = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result

# Test the function
print(add([4, 2, 6, 7]))  # Output: 2
print(add([1, 3, 5, 2]))  # Output: 2
print(add([2, 4, 6, 8]))  # Output: 12
print(add([3, 5, 7, 9]))  # Output: 0

# Check for invalid input
try:
    print(add([]))
except IndexError:
    print("Invalid input: List is empty")
try:
    print(add("Hello, World!"))
except TypeError:
    print("Invalid input: List contains non-integer elements")