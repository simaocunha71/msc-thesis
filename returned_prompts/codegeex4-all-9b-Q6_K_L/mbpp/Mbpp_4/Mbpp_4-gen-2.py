```python
def heap_queue_largest(lst, n):
    import heapq
    largest = heapq.nlargest(n, lst)
    return largest
```
