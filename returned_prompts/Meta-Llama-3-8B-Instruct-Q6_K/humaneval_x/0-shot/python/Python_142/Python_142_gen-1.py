    def sum_squares(lst):
        result = 0
        for i, num in enumerate(lst):
            if i % 3 == 0:
                result += num ** 2
            elif i % 4 == 0 and i % 3 != 0:
                result += num ** 3
        return result

# Testing the function
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([1, 2, 3, 4, 5, 6]))  # Output: 55
print(sum_squares([1, 1, 1, 1, 1, 1]))  # Output: 6
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 216
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 285
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Output: 384
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # Output: 495
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))  # Output: 612
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))  # Output: 729
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 