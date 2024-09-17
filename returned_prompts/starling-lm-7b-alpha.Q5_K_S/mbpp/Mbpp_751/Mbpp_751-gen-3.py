
def check_min_heap(heap):
    n = len(heap)
    for i in range(n // 2):
        if heap[i] > heap[2 * i + 1]:
            return False
        if 2 * i + 2 < n and heap[i] > heap[2 * i + 2]:
            return False
    return True


