"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""
class Solution:
    def extract_index(self, l1, l2, l3):
        """ Returns a list of common elements from three lists. (list) -> (list) """
        indexes = set()
        for i in range(len(l1)):
            if l1[i] == l2[i] and l1[i] == l3[i]:
                indexes.add((i, 0))

        common_indexes = []
        for index in indexes:
            common_indexes.append(index)
        return sorted(set([l1[i][1], l2[i][1], l3[i][1]]), key=lambda x:x[0])
