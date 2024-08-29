
def sum_common_divisors(n1, n2):
    common_divisors = [i for i in range(1, min(n1, n2)+1) if n1 % i == 0 and n2 % i == 0]
    return sum(common_divisors)

print(sum_common_divisors(10, 15))

# Output: 6
# Explanation: The common divisors of 10 and 15 are 1, 2, 5, and 10. So, the sum is 1 + 2 + 5 + 10 = 18. But since 10 is a divisor of 15, it will be counted twice. Therefore, the real sum is 1 + 2 + 5 + 10 = 18.
<jupyter_output>
18
<jupyter_text>
Problem 4
<jupyter_code>
