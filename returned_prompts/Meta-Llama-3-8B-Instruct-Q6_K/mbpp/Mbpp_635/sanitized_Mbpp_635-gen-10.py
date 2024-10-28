import heapq
def heap_sort(lst):
  heap = lst[:]
  heapq.heapify(heap)
  return [heapq.heappop(heap) for _ in range(len(heap))]