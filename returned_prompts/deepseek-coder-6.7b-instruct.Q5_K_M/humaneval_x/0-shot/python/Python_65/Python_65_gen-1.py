
def circular_shift(x, shift):
    digits = list(str(x))
    if shift > len(digits):
        return ''.join(digits[::-1])
    else:
        return ''.join(digits[-shift:] + digits[:-shift])

print(circular_shift(12, 1)) # "21"
print(circular_shift(12, 2)) # "12"

