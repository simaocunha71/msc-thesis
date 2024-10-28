import heapq
def min_k(lst: list, k: int) -> list:
  return heapq.nsmallest(k, lst, key = lambda x: x[1])