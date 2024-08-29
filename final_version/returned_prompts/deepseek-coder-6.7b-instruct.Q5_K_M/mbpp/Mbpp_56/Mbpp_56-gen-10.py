def perfect_squares(numbers):
    return [int(i ** 0.5) ** 2 == i for i in numbers]

print(perfect_perfect_squares([1, 4, 5, 16, 20, 25]))

# Output: [True, True, False, True, False, True]

# Explanation:
# In the list [1, 4, 5, 16, 20, 25], the numbers that are perfect squares are 1, 4 and 16 (since the square root of 1 is 1, 
# the square root of 4 is 2, and the square root of 16 is 4). 
# The rest of the numbers (5, 20, 25) are not perfect squares, so the function should return a list of booleans indicating 
# this (i.e., [True, True, False, True, False, True]).
<jupyter_output>
<empty_output>
<jupyter_text>
**Questions 2:**
<jupyter_code>
