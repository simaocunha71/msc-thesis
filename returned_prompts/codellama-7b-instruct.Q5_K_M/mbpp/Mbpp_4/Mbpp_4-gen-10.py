"""
import heapq

def heap_queue_largest(my_list, n):
    largest = []
    for num in my_list:
        heapq.heappush(largest, -num)
        if len(largest) > n:
            heapq.heappop(largest)
    return [-num for num in sorted(largest)]
"""
