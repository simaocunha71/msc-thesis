"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
class Solution:
    def indexMultiplication(self, tuples):
        """
        :type tuples: List[Tuple[int, ...]]
        :rtype: List[Tuple[int, ...]]
        """
        res=[]
        for idx in range(len(tuples)):
            res.append((tuple(map(lambda x:x*tuples[idx][idx], tuples[idx])))) # list comprehension to convert
            
        return tuple(set([tuple(i) for i in res]))
