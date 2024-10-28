import heapq

def heap_queue_largest(num_list, n):
    h = []
    for num in num_list:
        heapq.heappush(h, -num)
        if len(h) > n:
            heapq.heappop(h)
    return [-x for x in sorted(h, reverse=True)]



