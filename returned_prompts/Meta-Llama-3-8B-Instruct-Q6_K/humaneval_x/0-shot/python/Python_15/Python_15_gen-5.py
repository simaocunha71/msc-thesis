def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n + 1))

# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'