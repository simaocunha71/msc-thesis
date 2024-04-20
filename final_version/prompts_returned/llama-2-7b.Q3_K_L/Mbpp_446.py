"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
class Solution:
    def countOccurrences(self, tuples):
        '''return the occured number of elements in a tuple as a list'''
        for i, x in enumerate(tuples):
            if not isinstance(x[0],str) and len(set(x)) == 1:
                #if the length of element of a tuple is just one then it will be considered as string
                tuples.append((str(i),tuple([str(j)])))