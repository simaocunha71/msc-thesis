Yes, it is possible to do a binary search to find the right insertion point of a specified value in a sorted array in O(logn) time. Here's an example implementation:

```python
def right_insertion(lst, v):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > v:
            right = mid
        else:
            left = mid + 1
    return left
```

In this implementation, we start with a left pointer at the start of the list and a right pointer at the end of the list. We repeatedly calculate the mid-point and update the pointers based on whether the value at the mid-point is greater than the target value. Eventually, we find the index at which the target value should be inserted.

The time complexity of this implementation is O(logn) because at each step, we are reducing the search space by a factor of 2, and the maximum number of steps required is logn.

However, it's worth noting that the original implementation using a linear search (i.e., the first example) is simpler and more efficient for small lists. For example, if the list has only 100 elements, the original implementation will find the insertion point in at most 101 steps, while the binary search implementation will take at least 63 steps.

Overall, the choice between a linear search or a binary search for finding the right insertion point in a sorted array depends on the specific requirements and constraints of the problem you are solving.


```

```

```python

```python

```python