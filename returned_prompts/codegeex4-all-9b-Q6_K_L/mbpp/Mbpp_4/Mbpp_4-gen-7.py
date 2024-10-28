```python
def heap_queue_largest(nums, n):
    import heapq
    heap = []
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return sorted(heap, reverse=True)

assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
```
