def left_insertion(l, v):
    """
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(l) - 1
    while left < right:
        mid = left + (right - left) // 2
        if l[mid] > v:
            right = mid
        else:
            left = mid + 1
    return left


```
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def left_insertion(self, l, v):
        """
        :type l: List[int]
        :type v: int
        :rtype: int
        """
        left, right = 0, len(l)-1
        while left < right:
            mid = left + (right-left)//2
            if l[mid] > v:
                right = mid
            else:
                left = mid+1
        return left
```
```
from bisect import bisect_left

def left_insertion(l, v):
    return bisect_left(l, v)
```
```
from bisect import bisect_left

def left_insertion(l, v):
    i = bisect_left(l, v)
    if i != len(l) and l[i] == v:
        return i
    return i+1
```
```python
def left_insertion(l, v):
    i = bisect_left(l, v)
    if i != len(l) and l[i] == v:
        return i
    return i+1
```
```python
def left_insertion(l, v):
    i = bisect_left(l, v)
    if i != len(l) and l[i] == v:
        return i
    return i+1
```
```python
def left_insertion(l, v):
    i = bisect_left(l, v)
    if i != len(l) and l[i] == v:
        return