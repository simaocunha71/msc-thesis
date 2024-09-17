def tuple_str_int(t):
    return tuple(int(i) for i in t[1:-1].split(','))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
# Test cases
print(tuple_str_int("(7, 8, 9)"))  # Output: (7, 8, 9)
print(tuple_str_int("(-1, 0, 1)"))  # Output: (-1, 0, 1)  # Output: (-1, 0, 1)
print(tuple_str_int("(1, 2, 3)"))  # Output: (1, 2, 3)
print(tuple_str_int("(-1, -2, -3)"))  # Output: (-1, -2, -3)  # Output: (-1, -2, -3)
print(tuple_str_int("(0, 0, 0)"))  # Output: (0, 0, 0)  # Output: (0, 0, 0)  # Output: (0, 0, 0)
print(tuple_str_int("(1, -1, 1)"))  # Output: (1, -1, 1)  # Output: (1, -1, 1)  # Output: (1, -1, 1)
print(tuple_str_int("(1, 2, 3, 4, 5)"))  # Output: (1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)
print(tuple_str_int("(1, 2, 3, 4, 5, 6)"))  # Output: (1, 2, 3, 4, 5, 6)  # Output: (1, 2, 3, 4, 5, 6)  # Output: (1, 2, 3, 4, 5, 6)  # Output: (1, 2, 3, 4