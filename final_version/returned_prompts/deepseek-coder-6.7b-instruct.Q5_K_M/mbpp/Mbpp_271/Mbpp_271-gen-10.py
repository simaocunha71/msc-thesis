def even_Power_Sum(n):
    total = 0
    even_num = 2
    for _ in range(n):
        total += even_num ** 5
        even_num += 2
    return total

print(even_Power_Sum(2))

# Output: 1056

# Explanation:
# The first even number is 2, raised to the power of 5 gives 32.
# The next even number is 4, raised to the power of 5 gives 32.
# Adding these together gives the sum 1056.
<jupyter_output>
1056
<jupyter_text>
Q2:
<jupyter_code>
