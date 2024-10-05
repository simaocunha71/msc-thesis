
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]

print(circular_shift(12, 1))
print(circular_shift(12, 2))
print(circular_shift(1234, 3))
print(circular_shift(1234, 5))
print(circular_shift(12345, 0))
print(circular_shift(12345, 6))

"""
12345, 0: 12345
12345, 6: 54321
"""

