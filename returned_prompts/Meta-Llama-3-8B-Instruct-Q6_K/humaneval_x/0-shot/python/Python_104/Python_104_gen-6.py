def unique_digits(x):
    def has_even_digit(num):
        while num:
            digit = num % 10
            if digit % 2 == 0:
                return True
            num //= 10
        return False

    return sorted([i for i in x if not has_even_digit(i)])


# Testing the function
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []


# Explanation:
# We define a helper function has_even_digit to check if a number has any even digit.
# Then, we use a list comprehension to filter the input list x and keep only the numbers that don't have any even digit.
# Finally, we sort the resulting list and return it.

# Note: The problem statement is a bit unclear, but I assume that the input is a list of positive integers. If the input is a single number, we can modify the function accordingly.