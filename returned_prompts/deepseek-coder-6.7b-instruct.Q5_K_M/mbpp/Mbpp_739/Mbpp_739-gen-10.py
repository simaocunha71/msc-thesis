"""
Explanation:

The smallest triangular number with 2 digits is 10, and its index is 4.

The triangular numbers are calculated as n*(n+1)/2.

To find the index of a triangular number with n digits, we can use the quadratic formula, 
but it would be more efficient to iterate until we find a triangular number with n digits.

We can use the following steps to solve the problem:

1. Start with index 1.
2. Calculate the triangular number for the current index.
3. If the triangular number has n digits, return the index.
4. If not, increment the index and repeat the process.

The time complexity of this solution is O(n), where n is the number of digits.

Here is the Python code for the problem:

"""

def find_Index(n):
    index = 1
    while len(str(int((index*(index+1))/2))) < n:
        index += 1
    return index

print(find_Index(2))  # Output: 4

# Explanasions: 
# The function find_Index takes an integer n as input.
# The variable index is initialized to 1.
# The while loop continues until the number of digits in the triangular number for the current index is less than n.
# Inside the loop, the triangular number for the current index is calculated using the formula (index*(index+1))/2.
# The len function is used to calculate the number of digits in the triangular number.
# If the number of digits is less than n, the index is incremented by 1 and the loop continues.
# Once a triangular number with n digits is found, the index is returned.
# The loop ends when a triangular number with n digits is found, so the function returns the index of the smallest triangular number with n digits.
<jupyter_output>
4
<jupyter_text>
