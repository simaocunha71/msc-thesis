
import heapq
def heap_sort(lst: list) -> list:
  heapq.heapify(lst)
  return [heapq.heappop(lst) for _ in range(len(lst))]


