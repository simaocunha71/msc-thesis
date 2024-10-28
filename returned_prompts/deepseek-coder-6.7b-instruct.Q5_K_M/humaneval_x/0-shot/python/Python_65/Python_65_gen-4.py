
    digits = str(x)
    if shift >= len(digits):
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]

print(circular_shift(12, 1))
print(circular_shift(12, 2))

#Output:
#21
#12



#