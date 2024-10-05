
    def maximum(arr, k):
        arr.sort(reverse=True)
        return arr[:k]


    # Example 1:
    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))  # [-4, -3, 5]

    # Example 2:
    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))  # [4, 4]

    # Example 3:
    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))  # [2]


    # Time complexity: O(n log n), where n is the length of arr.
    # Space complexity: O(k), where k is the input parameter.
    # This solution sorts the array in descending order and then returns the first k elements.
    # The sort operation has a time complexity of O(n log n) and the slicing operation has a time complexity of O(k).
    # The space complexity is O(k) because a new list is created to store the k maximum numbers.
    # The sort operation is not in-place, so it uses additional space proportional to the size of the input.
    # The slicing operation is a O(k) operation and does not use additional space.

"""

    def maximum(arr, k):
        return sorted(arr, reverse=True)[:k]
"""

"""
    def maximum(arr, k):
        return heapq.nlargest(k, arr)
"""

"""
    def maximum(arr, k):
        h = []
        for num in arr:
            heapq.heappush(h, num)
        return [heapq.heappop(h) for _ in range(k)]
"""

"""
    def maximum(arr, k):
        return nlargest(k, arr)
"""

"""
    def maximum(arr, k):
        return sorted(arr, reverse=True)[:k]
"""

"""
    def maximum