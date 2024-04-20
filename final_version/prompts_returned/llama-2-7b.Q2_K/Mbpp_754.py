"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""
import unittest
from collections import deque

def extract_index(l: list):
    index = []

    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] == l[i]:
                index.append((j,i))
                break
                print('common: %s'%l[i])
    return index


def extract_index_list(l: list):
    return [v for (i, v) in extract_index(l)] if l else []

class TestFucntions(unittest.TestCase):
    def test_extract_index(self):
        self.assertTrue(extract_index([1, 2, 3]) == [(0, 0), (1, 1)])
        
        
if __name__=='__main__':
    unittest.main()