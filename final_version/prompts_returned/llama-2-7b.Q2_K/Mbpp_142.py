"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
import heapq
from typing import List
def count_samepair(a: List[int], b:List[int], c:List[int] ) -> int:
    hs = [heapq.heappop(a), heapq.heappop(b), heapq.heappop(c)]
    s = set([])
    for i in range(0, len(hs), 2):
        s|=set(hs[i:i+2])
    return len(s)