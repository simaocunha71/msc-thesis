"""
This problem can be solved by using a dynamic programming approach. We will create a list to store the maximum sum for each number n.

We start by initializing a list of size n+1 with 0's. Then, we loop from 2 to n+1 and for each i, we calculate the maximum sum by using the formula f(n) = max(f(n/2) + f(n/3) + f(n/4) + f(n/5), n), and store it in the list at index i.

Finally, we return the last element in the list which represents the maximum sum for n.
"""

def get_max_sum(n):
    # Initialize a list of size n+1 with 0's.
    max_sum = [0] * (n+1)
    
    # Loop from 2 to n+1.
    for i in range(2, n+1):
        # Calculate the maximum sum for i using the formula.
        max_sum[i] = max(max_sum[i//2] + max_sum[i//3] + max_sum[i//4] + max_sum[i//5], i)
    
    # Return the last element in the list which represents the maximum sum for n.
    return max_sum[n]

assert get_max_sum(60) == 106
"""
This solution has a time complexity of O(n) as we loop from 2 to n+1 once. The space complexity is also O(n) due to the list of size n+1.
"""

# Test cases
assert get_max_sum(2) == 2
assert get_max_sum(3) == 4
assert get_max_sum(4) == 6
assert get_max_sum(5) == 9
assert get_max_sum(6) == 12
assert get_max_sum(7) == 15
assert get_max_sum(8) == 19
assert get_max_sum(9) == 23
assert get_max_sum(10) == 28
assert get_max_sum(60) == 106
assert get_max_sum(10