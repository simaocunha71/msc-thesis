import heapq
def expensive_items(items, n):
    """Find the n most expensive items in a given dataset."""
    heap = []
    for item in items:
        heapq.heappush(heap, (-item['price'], item))
        if len(heap) > n:
            heapq.heappop(heap)
    return [item for _, item in heap]