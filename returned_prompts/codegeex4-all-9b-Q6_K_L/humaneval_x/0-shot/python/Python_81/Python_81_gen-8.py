def numerical_letter_grade(grades):
    return [chr(ord('A') + i) + '+' if g >= 4.0 - 0.3 * i else 'E' if g == 0.0 else chr(ord('A') + i) + ('+' if g >= 4.0 - 0.3 * (i+0.5) else '-') for i,g in enumerate(range(5))]

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5, 3.8, 2.9, 1.9, 0.9, 0.0]))