    def unique_digits(x):
        return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])

# Test cases
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []
print(unique_digits([11, 13, 15, 17]))  # [11, 13, 15, 17]  # No change, as all numbers are odd
print(unique_digits([2, 4, 6, 8, 10]))  # []  # No numbers have no even digits
print(unique_digits([1, 3, 5, 7, 9]))  # [1, 3, 5, 7, 9]  # All numbers are odd
print(unique_digits([142, 154, 166, 178, 190]))  # []  # No numbers have no even digits
print(unique_digits([13, 15, 17, 19, 21]))  # [13, 15, 17, 19, 21]  # All numbers are odd
print(unique_digits([12, 14, 16, 18, 20]))  # []  # No numbers have no even digits

# Testing for edge cases
print(unique_digits([1]))  # [1]
print(unique_digits([]))  # []
print(unique_digits([1, 2]))  # []
print(unique_digits([1, 3]))  # [1, 3]
print(unique_digits([1, 2, 3]))  # []
print(unique_digits([1, 2, 3, 4]))  # []
print(unique_digits([1, 2, 3, 4, 5]))  # [1, 3, 5]
print(unique_digits([1, 2, 3, 4, 5, 6]))  # []
print(unique_digits([1, 2, 3, 4, 5, 6, 7]))  # [1, 3, 5, 7]
print(unique_digits([1, 2, 3, 4, 5, 6, 7, 8]))  # []
print(unique_digits([1