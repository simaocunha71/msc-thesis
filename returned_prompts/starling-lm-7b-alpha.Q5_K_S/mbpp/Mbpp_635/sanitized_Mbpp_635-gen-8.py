import heapq
def heap_sort(lst):
    """Sort a list using heap sort."""
    heapq.heapify(lst)
    sorted_list = []
    while lst:
        sorted_list.append(heapq.heappop(lst))
    return sorted_list