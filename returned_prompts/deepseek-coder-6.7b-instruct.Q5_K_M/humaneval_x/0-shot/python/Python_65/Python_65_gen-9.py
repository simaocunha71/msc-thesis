
    x = str(x)
    if shift > len(x):
        return x[::-1]
    return x[-shift:] + x[:-shift]

print(circular_shift(12, 1))
print(circular_shift(12, 2))
print(circular_shift(12, 3))
print(circular_shift(12345, 2))
print(circular_shift(12345, 8))

This function works by converting the integer x to a string, then slicing the string at the point of the shift. If the shift is larger than the length of the string, it reverses the string. Otherwise, it concatenates the last shift digits of the string to the start of the string.
<jupyter_output>
21
12
123
34512
12345
<jupyter_text>
