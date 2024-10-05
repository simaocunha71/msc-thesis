
def circular_shift(x, shift):
    s = str(x)
    n = len(s)
    result = ""
    if shift >= n:
        return s[::-1]
    else:
        result = s[n - shift:] + s[:n - shift]
    return result

print(circular_shift(12, 1))
print(circular_shift(12, 2))

# Test Cases
print(circular_shift(1234, 1))  # 2341
print(circular_shift(1234, 2))  # 3412
print(circular_shift(1234, 3))  # 4123
print(circular_shift(1234, 4))  # 1234
print(circular_shift(1234, 5))  # 4321

# Test Cases with zero shift
print(circular_shift(1234, 0))  # 1234
print(circular_shift(0, 1))  # 0
print(circular_shift(0, 5))  # 0

# Test Cases with negative shift
print(circular_shift(1234, -1))  # 4231
print(circular_shift(1234, -2))  # 3412
print(circular_shift(1234, -3))  # 2341
print(circular_shift(1234, -4))  # 1234
print(circular_shift(1234, -5))  # 2341

# Test Cases with large shift
print(circular_shift(1234, 100))  # 4321
print(circular_shift(1234, 1000))  # 4321
print(circular_shift(1234, 10000))  # 4321
print(circular_shift(1234,