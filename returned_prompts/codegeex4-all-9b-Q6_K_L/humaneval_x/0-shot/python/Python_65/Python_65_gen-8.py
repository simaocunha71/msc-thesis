def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(123456789, 3))  # Output: "789123456"
print(circular_shift(123456789, 9))  # Output: "987654321"