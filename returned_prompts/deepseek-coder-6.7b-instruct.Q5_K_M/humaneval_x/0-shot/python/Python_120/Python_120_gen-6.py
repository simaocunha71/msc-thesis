
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    import heapq
    return sorted(heapq.nlargest(k, arr))

# Tests:
print(maximum([-3, -4, 5], 3))  # should return [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # should return [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # should return [2]

# This code defines the function maximum which takes an array of integers and a positive integer k as input and returns the maximum k numbers in arr in sorted order. The function uses the heapq.nlargest function from the heapq module to find the k largest numbers in arr. The results are then sorted and returned. The tests at the end of the code verify that the function works as expected.
<jupyter_output>
[-4, -3, 5]
[4, 4]
[2]
<jupyter_text>
Problem 14: Given an array of integers arr and a positive integer k, return a sorted list of length k with the