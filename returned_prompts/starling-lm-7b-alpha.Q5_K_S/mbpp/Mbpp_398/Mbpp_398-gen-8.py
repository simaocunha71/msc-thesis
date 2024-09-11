def sum_of_digits(lst):
    sums = 0
    for i in lst:
        while i:
            sums += i % 10
            i //= 10
    return sums


def test_sum_of_digits():
    assert sum_of_digits([10, 2, 56]) == 14
    print("All Tests Passed")


test_sum_of_digits()

# sum_of_digits([10,2,56])

"""
"""

"""
"""

"""

"""

#sum_of_digits([10,2,56])


# """
# def sum_of_digits(lst):
#     sums = 0
#     for i in lst:
#         while i:
#             sums += i % 10
#             i //= 10
#     return sums

# def test_sum_of_digits():
#     assert sum_of_digits([10, 2, 56]) == 14
#     print("All Tests Passed")

# test_sum_of_digits()

# sum_of_digits([10,2,56])



# """
# def sum_of_digits(lst):
#     sums = 0
#     for i in lst:
#         while i:
#             sums += i % 10
#             i //= 10
#     return sums

# def test_sum_of_digits():
#     assert sum_of_digits([10, 2, 56]) == 14
#     print("All Tests Passed")

# test_sum_of_digits()

# sum_of_digits([10,2,56])



# """
# def sum_of_digits(lst):
#     sums = 0
#     for i in lst:
#         while i:
#             sums += i % 10
#             i //= 1