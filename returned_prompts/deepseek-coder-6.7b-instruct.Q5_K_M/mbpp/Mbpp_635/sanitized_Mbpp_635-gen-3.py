def heap_sort(lst):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]