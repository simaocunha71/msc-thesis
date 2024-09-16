"""
The maximum product formed by multiplying numbers of an increasing subsequence of that array is the product of the last number of the subsequence.

We can find the maximum product by recursively multiplying the last number of an increasing subsequence with the maximum product formed by multiplying the rest of the numbers of the subsequence.
"""

def max_product(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        max_left = max_product(arr[:-1])
        max_right = max_product(arr[1:])
        max_mid = max(arr[-1], arr[-2])
        return max(max_left * max_mid, max_right * max_mid)

assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([3, 100, 4, 5, 150, 6, 200]) == 600000

"""
Time complexity: O(n)
Space complexity: O(n)
"""
