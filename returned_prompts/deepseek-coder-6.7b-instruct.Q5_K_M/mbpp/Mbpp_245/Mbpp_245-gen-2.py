"""
This problem can be solved by using dynamic programming. We can create two arrays, one to store the maximum sum of increasing subsequences and another for decreasing subsequences.

We iterate through the array from left to right, updating the increasing array at each step. We also calculate the maximum sum of the increasing subsequences up to that point.

Next, we iterate through the array from right to left, updating the decreasing array at each step. We also calculate the maximum sum of the decreasing subsequences up to that point.

Finally, we iterate through the arrays again, for each element we consider the maximum sum of the bitonic subsequence that includes the current element, which is the sum of the maximum sum of increasing subsequence up to the previous element and the maximum sum of decreasing subsequence up to the next element.

The maximum of these sums is the maximum sum of the bitonic subsequence for the given array.

Here is the Python code for the problem:
"""

def max_sum(arr):
    n = len(arr)
    inc = [0]*n
    dec = [0]*n

    # calculating increasing sum
    inc[0] = arr[0]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i]) if arr[i] > arr[i-1] else arr[i]

    # calculating decreasing sum
    dec[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i]) if arr[i] > arr[i+1] else arr[i]

    # calculating maximum sum of bitonic subsequences
    bitonic_sum = [0]*n
    for i in range(n):
        bitonic_sum[i] = inc[i] + dec[i] - arr[i] if inc[i] > dec[i] else inc[i] if inc[i] > arr[i] else dec[i] if dec[i] > arr[i] else arr[i]

    return max(bitonic_sum)

print(max_sum([1, 15, 51, 