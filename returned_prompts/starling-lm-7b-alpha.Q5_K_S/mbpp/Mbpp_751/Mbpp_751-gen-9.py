
def check_min_heap(heap):
    heap_size = len(heap)
    if heap_size == 0:
        return False
    for i in range(heap_size // 2, -1, -1):
        if heap[i] > heap[2 * i + 1]:
            return False
        if heap[i] > heap[2 * i + 2]:
            return False
    return True


