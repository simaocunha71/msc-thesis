
def heap_queue_largest(numbers, n):
    # create a min heap
    heap = list(numbers)
    heapq.heapify(heap)
    # remove n smallest
    for _ in range(len(heap) - n):
        heapq.heappop(heap)
    return heap

