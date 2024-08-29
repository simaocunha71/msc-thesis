def sum_average(n):
    sum_of_numbers = n * (n + 1) // 2
    avg = sum_of_numbers / n
    return (sum_of_numbers, avg)

print(sum_average(10))  # Should return (55, 5.5)

# Explanation:
# The sum of first n natural numbers is n*(n+1)/2.
# The average is the sum divided by n.
# We return both the sum and the average as a tuple.

# Note:
# The '//' operator is used for integer division in Python. It is equivalent to '/' but it always results in an integer.
# This function assumes that n is a positive integer. If n is not a positive integer, the function may not work as expected.
<jupyter_output>
(55, 5.5)
<jupyter_text>
Question 3
<jupyter_code>
