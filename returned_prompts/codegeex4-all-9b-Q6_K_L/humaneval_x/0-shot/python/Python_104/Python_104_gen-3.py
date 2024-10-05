def unique_digits(x):
    def has_even_digit(n):
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                return True
            n //= 10
        return False

    return sorted([num for num in x if not has_even_digit(num)])

print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []