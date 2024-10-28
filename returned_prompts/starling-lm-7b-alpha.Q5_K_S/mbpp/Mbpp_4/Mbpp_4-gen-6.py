from heapq import heapify,heappush,heappop
def heap_queue_largest(nums,k):
    heapify(nums)
    res=[]
    for i in range(k):
        res.append(heappop(nums))
    return res

"""
from heapq import heapify,heappush,heappop
def heap_queue_largest(nums,k):
    heap=[]
    for num in nums:
        heappush(heap,-num)
    res=[]
    for i in range(k):
        res.append(-heappop(heap))
    return res
"""


"""
from heapq import heapify,heappush,heappop
def heap_queue_largest(nums,k):
    heap=[0]*len(nums)
    for i,num in enumerate(nums):
        heappush(heap,num)
    res=[]
    for i in range(k):
        res.append(heappop(heap))
    return res
"""


"""
def heap_queue_largest(nums,k):
    heap=[0]*len(nums)
    for i,num in enumerate(nums):
        heap[i]=-num
    heapify(heap)
    res=[]
    for i in range(k):
        res.append(-heap[0])
        heappop(heap)
    return res
"""

"""
def heap_queue_largest(nums,k):
    heap=[0]*len(nums)
    for i,num in enumerate(nums):
        heap[i]=-num
    heapify(heap)
    res=[]
    for i in range(k):
        res.append(-heap[i])
    return res
"""

"""
def heap_queue_largest(nums,k):
    heap=[0]*len(nums)
    for i,num in enumerate(nums):
        heap[i]=-num
    heapify(heap)
    for i in range(len(heap)-1,len(heap)-1-k,-1