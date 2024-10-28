```
def heap_queue_largest(nums, n):
    import heapq
    return heapq.nlargest(n, nums)
```


The function `heap_queue_largest` takes a list of numbers `nums` and an integer `n` as input, and returns the `n` largest integers from `nums` in descending order.

The `heapq.nlargest` function is used to find the `n` largest elements from the input list `nums`. It returns a list of the `n` largest elements in descending order.

For example, if we call `heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3)`, it will return `[85, 75, 65]`, which are the 3 largest integers from the input list in descending order.

This function has a time complexity of O(n log k) where n is the number of elements in the input list and k is the number of largest elements to be found. This is because the `heapq.nlargest` function uses a heap data structure to find the k largest elements, and the time complexity of inserting k elements into a heap is O(k log n). The function also has a space complexity of O(k) as it needs to store the k largest elements in memory.