"""
The idea is to take the number and shift it to the left by d positions, then take the number and shift it to the right by 32-d positions to get the bits that got lost in the left shift.
"""

def left_rotate(n, d):
    return (n << d)|(n >> (32 - d))

assert left_rotate(16,2) == 64

# 64 is obtained by rotating the binary representation of 16 to the left by 2 positions, adding the bits that got lost in the left shift (which are the last 2 bits in the binary representation of 16), and then converting this result back to decimal.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Maximum Difference between two elements such that larger element appears after the smaller elementGiven an array arr[] of integers, find two numbers with the maximum difference given that the larger number must appear after the smaller number in arr[].
<jupyter_code>
def maxDiff(arr):
    n = len(arr)
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, n):
        diff = arr[i] - min_element
        max_diff = max(max_diff, diff)
        min_element = min(min_element, arr[i])

    return max_diff

arr = [1, 2, 90, 10, 110, 80]
print("Maximum difference is", maxDiff(arr))
<jupyter_output>
Maximum difference is 100
<jupyter_text>
Problem 3: Find the Kth smallest element in an unsorted arrayGiven an array and a number k, where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.
<jupyter_code>
def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [12