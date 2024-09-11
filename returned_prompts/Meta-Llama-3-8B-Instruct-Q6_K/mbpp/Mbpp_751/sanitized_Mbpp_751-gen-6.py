def check_min_heap(heap):
    for i in range(1, len(heap)):
        if heap[i-1] > heap[i]:
            return False
    return True