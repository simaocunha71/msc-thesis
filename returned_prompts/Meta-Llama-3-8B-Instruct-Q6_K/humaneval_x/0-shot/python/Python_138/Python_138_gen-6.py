    def is_equal_to_sum_even(n):
        for i in range(2, n//2 + 1, 2):
            for j in range(i, n//2 + 1, 2):
                for k in range(j, n//2 + 1, 2):
                    for l in range(k, n//2 + 1, 2):
                        if i + j + k + l == n:
                            return True
        return False

# Test the function
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(10))  # True
print(is_equal_to_sum_even(12))  # True
print(is_equal_to_sum_even(14))  # True
print(is_equal_to_sum_even(16))  # True
print(is_equal_to_sum_even(18))  # True
print(is_equal_to_sum_even(20))  # True
print(is_equal_to_sum_even(22))  # True
print(is_equal_to_sum_even(24))  # True
print(is_equal_to_sum_even(26))  # True
print(is_equal_to_sum_even(28))  # True
print(is_equal_to_sum_even(30))  # True
print(is_equal_to_sum_even(32))  # True
print(is_equal_to_sum_even(34))  # True
print(is_equal_to_sum_even(36))  # True
print(is_equal_to_sum_even(38))  # True
print(is_equal_to_sum_even(40))  # True
print(is_equal_to_sum_even(42))  # True
print(is_equal_to_sum_even(44))  # True
print(is_equal_to_sum_even(46))  # True
print(is_equal_to_sum_even(48))  # True
print(is_equal_to_sum_even(50))  # True
print(is_equal_to_sum_even(52))  # True
print(is_equal_to_sum_even(54))  # True
print(is_equal_to_sum_even(56))  # True
print(is_equal_to_sum_even(58))  # True
print(is_equal_to_sum_even(60))  # True
print(is_equal_to_sum_even(62))  # True
print(is_equal_to_sum_even(64))  # True
print(is_equal_to_sum_even