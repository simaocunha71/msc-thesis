import heapq
def heap_sort(lst):
    heapq.heapify(lst)
    sorted_lst = [heapq.heappop(lst) for _ in range(len(lst))]
    return sorted_lst