
# Time:  O(nlogk)
# Space: O(1)

from heapq import heappushpop

class Solution(object):
    def maximum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        max_heap = []
        for x in arr:
            heappushpop(max_heap, x)
            if len(max_heap) > k:
                heappushpop(max_heap, max_heap[0])
            result.append(max_heap[0])
        return result


```

```
class Solution(object):
    def maximum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        max_heap = arr[:k]
        heapq.heapify(max_heap)
        for i in range(k,len(arr)):
            if arr[i] > max_heap[0]:
                heapq.heappush(max_heap, arr[i])
                heapq.heappop(max_heap)
        return list(max_heap)
```
```

```
def maximum(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    arr.sort(reverse=True)
    return arr[:k]
```

```

```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```