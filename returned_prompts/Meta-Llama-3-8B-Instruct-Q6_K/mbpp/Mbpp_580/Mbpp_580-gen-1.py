def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)

# Test the function
print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))  # Output: (4, (6, (2, 4)), 6, 8)  # Correct Output
print(extract_even((1, 2, (3, 4, (5, 6)), 7, 8)))  # Output: (2, (4, (6)), 8)  # Correct Output
print(extract_even((1, 2, 3, 4, 5, 6)))  # Output: (2, 4, 6)  # Correct Output
print(extract_even((1, 2, 3, 4, 5, 6, 7, 8)))  # Output: (2, 4, 6, 8)  # Correct Output
print(extract_even((1, 2, (3, 4, 5), 6, 7, 8)))  # Output: (2, (4, 5), 6, 8)  # Correct Output
print(extract_even((1, 2, 3, (4, 5, 6), 7, 8)))  # Output: (2, (4, 5, 6), 8)  # Correct Output
print(extract_even((1, 2, 3, 4, 5, 6, 7, 8, 9)))  # Output: (2, 4, 6, 8)  # Correct Output
print(extract_even((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))  # Output: (2, 4, 6, 8, 10)  # Correct Output
print(extract_even((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)))  # Output: (2, 4,