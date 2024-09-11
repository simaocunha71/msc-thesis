import heapq
def heap_sort(lst):
  heap = []
  for num in lst:
    heapq.heappush(heap, num)
  sorted_lst = []
  while heap:
    sorted_lst.append(heapq.heappop(heap))
  return sorted_lst