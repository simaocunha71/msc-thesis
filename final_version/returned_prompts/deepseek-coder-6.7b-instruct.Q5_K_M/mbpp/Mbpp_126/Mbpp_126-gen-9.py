def sum_common_divisors(n1, n2):
    def common_divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)
    return sum(common_divisors(n1) & common_divisors(n2))

print(sum_common_divisors(10, 15))

# Output:
# 6

# Explanation:
# The common divisors of 10 and 15 are 1, 2, 5, 10 and 15 itself. So, the sum is 1 + 2 + 5 + 10 + 15 = 36.


