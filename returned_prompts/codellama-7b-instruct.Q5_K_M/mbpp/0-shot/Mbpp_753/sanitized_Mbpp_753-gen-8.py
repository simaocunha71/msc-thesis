from heapq import heappush, heappop
def min_k(t, k):
    h = []
    for name, score in t:
        heappush(h, (-score, name))
        if len(h) > k:
            heappop(h)
    return [name for score, name in sorted(h)]