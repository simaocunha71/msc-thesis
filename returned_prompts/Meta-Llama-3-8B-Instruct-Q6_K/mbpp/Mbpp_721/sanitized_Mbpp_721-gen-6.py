import heapq
def maxAverageOfPath(costs):
    n = len(costs)
    max_heap = [(costs[0][0], 1, 0, 0)]
    max_average = 0
    for i in range(1, n):
        new_max_heap = []
        for _ in range(len(max_heap)):
            x, count, x_i, y_i = heapq.heappop(max_heap)
            if x_i < i:
                heapq.heappush(new_max_heap, (x + costs[i][x_i], count + 1, i, x_i))
                heapq.heappush(new_max_heap, (x + costs[i][x_i + 1], count + 1, i, x_i + 1))
        max_heap = new_max_heap
        while max_heap:
            x, count, i, y_i = heapq.heappop(max_heap)
            max_average = max(max_average, x / count)
    return max_average