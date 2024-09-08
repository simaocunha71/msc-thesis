def heap_queue_largest(lst, n):
    import heapq
    heapq.heapify(lst)
    return sorted([heapq.heappop(lst) for _ in range(n)], reverse=True)