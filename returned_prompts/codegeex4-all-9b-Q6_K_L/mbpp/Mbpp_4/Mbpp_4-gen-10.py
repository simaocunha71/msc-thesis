```python
def heap_queue_largest(numbers, n):
    import heapq
    # Create a max heap
    heap = [-x for x in numbers]
    heapq.heapify(heap)
    # Extract the n largest elements
    largest = [-heapq.heappop(heap) for _ in range(n)]
    # Return the elements in descending order
    return largest[::-1]
```