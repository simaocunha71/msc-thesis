Here is a Python solution using the heapq module, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. The n largest elements are found by first converting the list to a heap, then repeatedly removing and returning the smallest element from the heap until only the n largest elements remain.

```python
import heapq

def heap_queue_largest(lst, n):
    return heapq.nlargest(n, lst)
```

You can test this function with the provided assertion:

```python
assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
```

This will not throw an assertion error if the function is correct.