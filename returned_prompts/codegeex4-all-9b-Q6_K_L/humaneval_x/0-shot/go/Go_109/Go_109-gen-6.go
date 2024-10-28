```python
class Solution:
    def moveOneBall(self, arr):
        if len(arr) == 0:
            return True
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                return False
        return True
```
