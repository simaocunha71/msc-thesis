"""
def heap_queue_largest(nums, k):
    import heapq
    heap = heapq.nlargest(k, nums)
    heapq.heapify(heap)
    return heap

# Test
nums = [25, 35, 22, 85, 14, 65, 75, 22, 58]
k = 3
print(heap_queue_largest(nums,k))
"""

# 解析
"""
使用heapq模块
heapq.nlargest(k, nums)返回从大到小排列的前k个数
heapq.heapify(heap)将heap列表转换为小顶堆
heapq.nlargest(k, nums)是O(nlogk)
heapq.heapify(heap)是O(n)
"""

# 解答
```
import heapq

def heap_queue_largest(nums, k):
    heap = heapq.nlargest(k, nums)
    heapq.heapify(heap)
    return heap

# Test
nums = [25, 35, 22, 85, 14, 65, 75, 22, 58]
k = 3
print(heap_queue_largest(nums,k))
```

解析：
使用heapq模块，heap_queue_largest函数接收两个参数，nums和k，nums是原始列表，k是需要返回的最大数量。heap_queue_largest函数使用heapq.nlargest(k, nums)返回从大到小排列的前k个数，并将其存储到heap变量中。然后，heapq.heapify(heap)将heap列表转换为小顶堆。最后，heap_queue_largest函数返回heap列表。

测试：
nums = [25, 35, 22, 85, 14, 65, 75