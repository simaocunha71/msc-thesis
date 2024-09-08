def sum_digits(n):
    sum_num = 0
    while n:
        sum_num += n % 10
        n //= 10
    return sum_num

print(sum_digits(345))

# 345 // 10 = 34, 34 % 10 = 4
# 34 // 10 = 3, 3 % 10 = 3
# 3 // 10 = 0, 0 % 10 = 0

# sum_num = 0 + 4 + 3 + 3 = 10
assert sum_digits(345)==10

print("Correct")

# 345 is not a non-negative integer
# because the number has a negative sign in it.
# The function will not work correctly with negative integers.
# The function should be tested with non-negative integers.
<jupyter_output>
Correct
<jupyter_text>
Problem 2
<jupyter_code>
