def circular_shift(x, shift):
    s = str(x)
    if shift >= len(s):
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]

print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"