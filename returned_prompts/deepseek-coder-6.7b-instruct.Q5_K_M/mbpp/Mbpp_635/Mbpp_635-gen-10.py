
import heapq
def heap_sort(arr: list) -> list:
  heapq.heapify(arr)
  sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
  return sorted_arr


