"""
The idea is to perform binary search on the smaller array and then calculate the position in the larger array.

The function is as follows:
"""

def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    len1 = len(arr1)
    len2 = len(arr2)

    start = 0
    end = len1

    while start <= end:
        partition1 = (start + end) // 2
        partition2 = k - partition1

        l1 = arr1[partition1 - 1] if partition1 > 0 else float('-inf')
        l2 = arr2[partition2 - 1] if partition2 > 0 else float('-inf')
        r1 = arr1[partition1] if partition1 < len1 else float('inf')
        r2 = arr2[partition2] if partition2 < len2 else float('inf')

        if l1 > r2:
            end = partition1 - 1
        elif l2 > r1:
            start = partition1 + 1
        else:
            return max(l1, l2)

    return -1

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))

# Time complexity: O(log(min(m, n)))
# Space complexity: O(1)

# The function first checks if the first array is smaller than the second. If it is, it swaps the two arrays. It then initializes the start and end variables, which will be used for the binary search. It then enters a while loop, which continues until the start is less than or equal to the end.
# Inside the loop, it calculates the partitions for the two arrays, and the elements at these partitions. It then checks if the last element of the first partition is greater than the first element of the second partition. If it is, it adjusts the end variable for the binary search. If the first element of the second partition is greater than the last element of the first partition, it adjusts the start variable for the binary search