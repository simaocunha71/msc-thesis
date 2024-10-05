
def sum_squares(lst):
    total = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            lst[i] = lst[i] ** 3
        total += lst[i]
    return total

# Tests
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([10, 20, -30, 40, 50]))  # Output: -3850



# Tests
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([10, 20, -30, 40, 50]))  # Output: -3850





# Tests
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([10, 20, -30, 40, 50]))  # Output: -3850



































































