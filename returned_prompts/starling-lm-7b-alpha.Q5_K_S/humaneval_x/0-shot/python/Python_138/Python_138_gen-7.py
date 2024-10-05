    # if n % 4 != 0:
    #     return False
    # for i in range(1, n + 1):
    #     if i % 2 == 0:
    #         if i > n:
    #             continue
    #         for j in range(i + 1, n + 1):
    #             if j % 2 == 0:
    #                 if j > n:
    #                     continue
    #                 for k in range(j + 1, n + 1):
    #                     if k % 2 == 0:
    #                         if k > n:
    #                             continue
    #                         for l in range(k + 1, n + 1):
    #                             if l % 2 == 0:
    #                                 if l > n:
    #                                     continue
    #                                 if i + j + k + l == n:
    #                                     return True
    # return False
    return sum([i for i in range(0, n + 1, 2) if i <= n]) == n


# print(is_equal_to_sum_even(4))
# print(is_equal_to_sum_even(6))
# print(is_equal_to_sum_even(8))
# print(is_equal_to_sum_even(9))
# print(is_equal_to_sum_even(10))


def is_equal_to_sum_even(n):
    if n % 4 != 0:
        return False
    for i in range(1, n + 1, 2):
        for j in range(i + 1, n + 1, 2):
            for k in range(j + 1, n + 1, 2):
                for l in range(k + 1, n + 1, 2):
                    if i + j + k + l == n:
                        return True
    return False


print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print