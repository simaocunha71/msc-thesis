def heap_sort(lst):
    if len(lst) <= 1:
        return lst
    heap = []
    for num in lst:
        heapq.heappush(heap, num)
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list