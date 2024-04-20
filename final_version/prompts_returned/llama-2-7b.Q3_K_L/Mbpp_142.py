"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
from typing import List

def count_samepair(a:List[int],b:List[int],c:List[int]) -> int:
    # 普通的做法有多种，这里来一个比较简单的解决方案
    if len(a) == len(b) and len(c) == len(b):
        res = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                print('第%d个相同' % (i+1))
                res += 1
            else:
                break
    return res

print(count_samepair([2,3,5,6],[4,2,3,1], [3,2,1,2]))