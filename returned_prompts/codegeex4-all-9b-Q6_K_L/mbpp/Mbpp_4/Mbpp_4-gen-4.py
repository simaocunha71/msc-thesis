```python
def heap_queue_largest(lst, n):
    import heapq
    heapq.heapify(lst)
    return sorted([heapq.heappop(lst) for _ in range(n)], reverse=True)

assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
```