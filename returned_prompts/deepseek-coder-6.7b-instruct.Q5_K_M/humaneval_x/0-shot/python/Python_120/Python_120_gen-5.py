
    arr = sorted(arr)
    return arr[-k:]

# Test cases
print(maximum([-3, -4, 5], 3)) # [-4, -3, 5]
print(maximum([4, -4, 4], 2)) # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1)) # [2]

The function sorts the array in ascending order and then returns the last k elements from the sorted array.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(k) as we are storing the last k elements of the array.

This solution assumes that arr[i] is the i-th smallest number in the array. If this is not the case, then you should use a different strategy to find the k largest numbers.
"""

def maximum(arr, k):
    import heapq
    return heapq.nlargest(k, arr)

# Test cases
print(maximum([-3, -4, 5], 3)) # [-4, -3, 5]
print(maximum([4, -4, 4], 2)) # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1)) # [2]

"""
In the above solution, we use the heapq library in python which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. heapq.nlargest(n, iterable) function returns the n largest elements from the iterable, in descending order.

The time complexity of this solution is O(n log k) because the heapify operation (which is the most time-consuming operation) is O(log k) and we perform this operation n times. The space complexity is O(k) as we are storing the k largest elements of the array.

This solution assumes that arr[i] is the i-th smallest number in the array. If this is not the case, then you should use a different strategy to find the k largest numbers