
class Solution:
    def maximum(self, arr, k):
        arr.sort()
        return arr[-k:]

B:

def maximum(arr, k):
    arr = sorted(arr)
    return arr[-k:]

C:

from heapq import nlargest

def maximum(arr, k):
    return nlargest(k, arr)