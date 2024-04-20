"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. 
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
class Solution(object):
    def tupleToDict(self, tup):
        """
        :type tup: Tuple[int]
        :rtype: dict(int, int)
        """
        if not tup or len(tup) == 0:
            return {0:-1}
        
        dct = {}
        for i in xrange(len(tup)):
            if tup[i] - tup[i-1] != 2 and (i < 3 or tup[i+1] == tup[i]+2): # If last 2 elements are adjacent then there is no need for dict entry.
                dct[(tup[i], tup[i])] = i - 1 
        return dct