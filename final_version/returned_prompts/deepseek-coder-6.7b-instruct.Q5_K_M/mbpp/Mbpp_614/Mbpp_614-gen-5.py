
def cummulative_sum(lst):
    total_sum = 0
    for tup in lst:
        total_sum += sum(tup)
    return total_sum

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))  # 30

"""
The function `cummulative_sum` takes a list of tuples as input.
It initializes a variable `total_sum` to 0.
Then it iterates over each tuple in the list. For each tuple, it adds the sum of its elements to `total_sum`.
Finally, it returns `total_sum`.
"""

# In the example given, the list contains three tuples. 
# The first tuple contains the numbers 1 and 3, so its sum is 1 + 3 = 4.
# The second tuple contains the numbers 5, 6, and 7, so its sum is 5 + 6 + 7 = 18.
# The third tuple contains the numbers 2 and 6, so its sum is 2 + 6 = 8.
# The cumulative sum of these values is 4 + 18 + 8 = 30.
# So the function correctly returns 30.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5
<jupyter_code>
