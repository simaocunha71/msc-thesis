def sum_common_divisors(num1, num2):
    def common_divisors(num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    divisors1 = common_divisors(num1)
    divisors2 = common_divisors(num2)
    common = set(divisors1) & set(divisors2)
    return sum(common)

# Testing
assert sum_common_divisors(10, 15) == 6
print(f'Test case passed.')

# Testing
assert sum_common_divisors(7, 4) == 3
print(f'Test case passed.')

# Testing
assert sum_common_divisors(11, 12) == 3
print(f'Test case passed.')

# Testing
assert sum_common_divisors(100, 200) == 100
print(f'Test case passed.')

# Testing
assert sum_common_divisors(1000, 2000) == 1000
print(f'Test case passed.')

# Testing
assert sum_common_divisors(500, 600) == 100
print(f'Test case passed.')

# Testing
assert sum_common_divisors(1000000, 2000000) == 1000000
print(f'Test case passed.')

# Testing
assert sum_common_divisors(3, 4) == 1
print(f'Test case passed.')

# Testing
assert sum_common_divisors(1, 2) == 1
print(f'Test case passed.')

# Testing
assert sum_common_divisors(2, 3) == 1
print(f'Test case passed.')

# Testing
assert sum_common_div