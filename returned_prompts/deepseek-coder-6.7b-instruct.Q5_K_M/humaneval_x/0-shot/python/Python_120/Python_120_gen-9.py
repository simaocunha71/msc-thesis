
    def maximum(arr, k):
        arr.sort()
        return arr[-k:]

    print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
    print(maximum([4, -4, 4], 2))  # [4, 4]
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]

This solution works by first sorting the array in ascending order, then returning the last k elements of the sorted array. This will be the k largest numbers in the array.

The time complexity is O(n log n), due to the sort operation, where n is the length of the array. The space complexity is O(k), as we are returning a list of k elements.
"""

def maximum(arr, k):
    arr.sort()
    return arr[-k:]

print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]

# Alternative solution using heapq

"""
import heapq

def maximum(arr, k):
    return heapq.nlargest(k, arr)

print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]

This solution works by using the nlargest function from the heapq module, which returns the k largest elements from the array in descending order.

The time complexity is O(n log k) due to the nlargest operation, where n is the length of the array. The space complexity is O(k), as we