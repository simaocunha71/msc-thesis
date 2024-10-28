
import heapq as hq
def heap_sort(my_list: list) -> list:
  hq.heapify(my_list)
  my_list.sort()
  return my_list


