
def sum_squares(lst):
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += lst[i] ** 3
    return result


# Testing
print(sum_squares([1, 2, 3]))  # Expected output: 6
print(sum_squares([]))  # Expected output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Expected output: -126








```
