def is_equal_to_sum_even(n):
    if n < 8:
        return False
    for i in range(2, n, 2):
        for j in range(i, n, 2):
            for k in range(j, n, 2):
                for l in range(k, n, 2):
                    if i + j + k + l == n:
                        return True
    return False

print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True