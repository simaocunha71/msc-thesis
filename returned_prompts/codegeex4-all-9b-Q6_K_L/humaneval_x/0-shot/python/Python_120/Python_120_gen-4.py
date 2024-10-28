Here is a solution in Python:

```python
def maximum(arr, k):
    arr.sort(reverse=True)
    return arr[:k]
```

In this solution, we first sort the array in descending order. Then we return the first k elements of the sorted array. The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the array.

If you want a solution with a better time complexity, you can use the heap data structure. Here is a solution in Python:

```python
import heapq

def maximum(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
    return sorted(heap)
```

In this solution, we first create a min heap with the first k elements of the array. Then we iterate over the remaining elements of the array. If the current element is larger than the smallest element in the heap, we remove the smallest element from the heap and add the current element to the heap. Finally, we return the sorted heap. The time complexity of this solution is O(n log k), where n is the length of the array and k is the size of the heap.