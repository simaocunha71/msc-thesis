import heapq
def min_k(tup_list, k):
  return heapq.nsmallest(k, tup_list, key = lambda x: x[1])