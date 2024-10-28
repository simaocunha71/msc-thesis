def circular_shift(x, shift):
    x_str = str(x)
    if shift >= len(x_str):
        return x_str[::-1]
    else:
        return x_str[-shift:] + x_str[:-shift]

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(12345, 3))  # Output: "34512"
print(circular_shift(12345, 5))  # Output: "54321"