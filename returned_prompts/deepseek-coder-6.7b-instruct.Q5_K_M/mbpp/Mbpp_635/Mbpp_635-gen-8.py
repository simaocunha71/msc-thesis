
import heapq as hq
def heap_sort(lst: list) -> list:
  hq.heapify(lst)
  return [hq.heappop(lst) for _ in range(len(lst))]


