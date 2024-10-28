```python
def heap_queue_largest(numbers, n):
    import heapq
    heap = heapq.nlargest(n, numbers)
    return heap

assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
```