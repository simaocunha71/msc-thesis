"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
class Solution:
    def tupleToInt(self, A):
        if type(A) is tuple and len(A) == 0: return 0
        res = reduce(lambda x,y:x+y, A)+int("".join([str(x) for x in A]))
        return int(res)