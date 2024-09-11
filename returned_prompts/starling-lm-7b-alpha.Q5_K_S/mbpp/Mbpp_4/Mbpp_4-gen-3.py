"""
def heap_queue_largest(nums,n):
    import heapq
    heap = []
    for i in nums:
        heapq.heappush(heap, -i)
    res = []
    for i in range(n):
        res.append(-heapq.heappop(heap))
    return res

# Testing
print(heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)) # [85, 75, 65]

"""

def heap_queue_largest(nums,n):
    import heapq
    heap = []
    for i in nums:
        heapq.heappush(heap, -i)
    res = []
    for i in range(n):
        res.append(-heapq.heappop(heap))
    return res

# Testing
print(heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)) # [85, 75, 65]



















"""



































































































































































































