"""
We need to use Dynamic Programming to solve this problem.

We create a list to store the maximum sum for each number. Then we use the equation to calculate the maximum sum for each number.

Finally, we return the maximum sum for the given number n.
"""

def get_max_sum(n):
    # Initialize a list to store the maximum sum for each number
    sums = [0]*(n+1)
    
    # Calculate the maximum sum for each number
    for i in range(1, n+1):
        sums[i] = max(sums[i//2]+sums[i//3]+sums[i//4]+sums[i//5], i)
    
    # Return the maximum sum for the given number n
    return sums[n]

# Test the function
assert get_max_sum(60) == 106
"""
This function works by first initializing an array with zeros of length n+1. This array will be used to store the maximum sum that can be obtained by considering numbers from 1 to n.

The function then iterates over each number from 1 to n, calculating the maximum sum that can be obtained by considering that number as well as the sums of the numbers divided by 2, 3, 4, and 5. The maximum of these sums is stored in the array for that number.

Finally, the function returns the maximum sum that can be obtained by considering numbers from 1 to n.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
