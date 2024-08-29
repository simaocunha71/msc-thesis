def sum_average(n):
    total_sum = n * (n + 1) // 2
    average = total_sum / n
    return (total_sum, average)

print(sum_average(10))  # Output: (55, 5.5)

"""
Explanation:
The sum of first n natural numbers can be calculated using the formula: n*(n+1)/2
The average is simply the total sum divided by n.
"""
<jupyter_output>
(55, 5.5)
<jupyter_text>
Question 2:
<jupyter_code>
