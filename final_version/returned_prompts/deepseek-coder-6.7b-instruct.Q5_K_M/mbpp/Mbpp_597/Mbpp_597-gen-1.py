
def find_kth(arr1, arr2, k):
    # merge the two arrays
    merged = sorted(arr1 + arr2)
    # kth element is at index k-1 in the merged array
    return merged[k - 1]

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8,, 10], 5))
"""
This solution works well, but it's not the most efficient solution. The time complexity is O(n log n) because of the sorting operation. 
If you're dealing with large lists, this solution may not be the best.

A more efficient solution is to use a two-pointer technique, which has a time complexity of O(k). The idea is to keep track of the kth element we've found so far and the index of the next element in each list to compare.
"""

def find_kth(arr1, arr2, k):
    i = j = 0
    result = None
    while i + j < k:
        if i == len(arr1):
            result = arr2[j]
            j += 1
        elif j == len(arr2):
            result = arr1[i]
            i += 1
        elif arr1[i] < arr2[j]:
            result = arr1[i]
            i += 1
        else:
            result = arr2[j]
            j += 1
    return result

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))

# This solution works by maintaining two pointers, one for each list. The pointer that points to the smaller element is moved to the next element in its list. The process is repeated until the kth element is found.

# The time complexity of this solution is O(k), and it is more efficient for large lists.

# Please note that the array indices in python start from 0, so when we say 'kth' we start counting from 1 (i.e., the first element is '1st'). So in the examples above, 6 is the 5th