def unique_digits(x):
    def has_even_digit(n):
        return any(digit % 2 == 0 for digit in str(n))
    return sorted([n for n in x if not has_even_digit(n)])

print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))