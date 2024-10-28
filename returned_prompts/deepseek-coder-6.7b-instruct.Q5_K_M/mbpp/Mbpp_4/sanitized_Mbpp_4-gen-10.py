def heap_queue_largest(lst: list, n: int) -> list:
    import heapq
    return heapq.nlargest(n, lst)