    if n % 4 != 0:
        return False
    n = n / 4
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                for l in range(n + 1):
                    if i + j + k + l == n:
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                            return True
    return False


# Here are some test cases for reference. Feel free to add more of your own.
# Note that these test cases are designed to cover all the branches in the code.
assert(is_equal_to_sum_even(4) == False)
assert(is_equal_to_sum_even(6) == False)
assert(is_equal_to_sum_even(8) == True)
assert(is_equal_to_sum_even(2) == False)
assert(is_equal_to_sum_even(10) == True)
assert(is_equal_to_sum_even(12) == True)
assert(is_equal_to_sum_even(14) == True)
assert(is_equal_to_sum_even(16) == True)
assert(is_equal_to_sum_even(18) == True)
assert(is_equal_to_sum_even(20) == True)




























































































































































