"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
class Solution:
    def countFirstElements(self, tuples):
        """
        :param tuples: [(i, j)]
        :return: j
        """
        index = []
        for element in tuples:
            if element[0] == element[1]:
                index.append(element)
                continue
            
            index.append([element])
        n = 0
        for i, j in enumerate(index):
            print('n', n + j[-1][-2])
            if n+j[-1][-2] == tuples[i][1]:
                return n + j[-1][-2] - tuples[i][0]
            else:
                n += 1
        return n
