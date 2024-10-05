def unique_digits(x):
    def is_unique(num):
        digits = set(str(num))
        return all(int(digit) % 2 != 0 for digit in digits)
    return sorted([num for num in x if is_unique(num)])

print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))