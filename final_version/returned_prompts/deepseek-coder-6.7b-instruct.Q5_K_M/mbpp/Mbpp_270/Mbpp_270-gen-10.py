def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum

assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
The function sum_even_and_even_index takes a list as an argument. It initializes a variable sum to 0. 
It then uses a for loop to iterate over the elements in the list at even positions. 
If the element at the current position is even (i.e., its remainder when divided by 2 is 0), it adds the element to sum. 
The function then returns the sum.
"""

# End of Solution
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
# Solution

