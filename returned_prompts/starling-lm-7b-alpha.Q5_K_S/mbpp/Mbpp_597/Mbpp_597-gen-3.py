"""
def find_kth(A, B, k):
    if k > len(A):
        return B[k - len(A) - 1]
    elif k > len(B):
        return A[k - len(B) - 1]
    elif A[k - 1] > B[k - 1]:
        return find_kth(A, B, k - 1)
    else:
        return find_kth(A, B, k)
"""

def find_kth(A, B, k):
    l = 0
    r = len(A) + len(B)

    while l < r:
        m = (l + r) // 2
        if A[m // len(A)] < B[m % len(B)]:
            l = m + 1
        else:
            r = m
    return A[l // len(A)]

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6

"""
This problem can be solved using two pointers, which are pointed at the last elements of the two arrays.
The two pointers move to the left, and the one that moves to the left more times is the one from the array with the kth element.
The function then recursively calls itself with the two pointers, and the number of elements moved to the left in each array is added to k.
If the kth element is in the first array, the function returns the kth element from the first array.
If the kth element is in the second array, the function returns the kth element from the second array.
"""

"""
Time complexity: O(log(min(len(A), len(B))))
Space complexity: O(1)
"""

```
  
# Python program to find kth element from two sorted arrays
from sys import stdin, stdout

def find_kth(A, B, k):
    # If k is greater than the length of the first array
    if k > len(A):
        # Return the kth element from the second array
        return