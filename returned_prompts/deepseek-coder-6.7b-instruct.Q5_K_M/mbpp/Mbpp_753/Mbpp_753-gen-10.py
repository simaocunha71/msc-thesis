
import heapq
def min_k(lst, k):
  return heapq.nsmallest(k, lst, key = lambda x: x[1])


