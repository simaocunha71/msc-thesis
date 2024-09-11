import heapq
def larg_nnum(nums, n):
  return heapq.nlargest(n, nums)  # returns the n largest items from the list