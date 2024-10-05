Here is a Python solution using heap data structure:

```python
import heapq

def maximum(arr, k):
    # Create a max heap
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    # Extract the k maximum elements
    result = [-heapq.heappop(max_heap) for _ in range(k)]

    # Sort the result
    result.sort()
    
    return result
```

This solution works by first creating a max heap from the input array. The Python heapq library provides an implementation of the heap data structure. The max heap is created by negating the elements of the input array, which effectively turns the min heap provided by the heapq library into a max heap.

Then, the k maximum elements are extracted from the heap and added to the result list. Finally, the result list is sorted and returned.

The time complexity of this solution is O(n log n), where n is the length of the input array. This is because creating a heap takes O(n) time, and extracting k elements from the heap and sorting the result takes O(k log k) time. The space complexity is O(n), which is required for the heap.