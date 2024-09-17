```python
def heap_queue_largest(nums, n):
    import heapq
    largest = heapq.nlargest(n, nums)
    return largest

assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
```
