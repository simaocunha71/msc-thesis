"""
def search(arr):
    x = arr[-1]
    while arr:
        if x == arr[-1]:
            arr.pop()
        else:
            break
    return arr[0]
"""

def search(arr):
    x = arr[-1]
    while arr:
        if x == arr[-1]:
            arr.pop()
        else:
            break
    return arr[0]

import unittest
class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([1, 1, 2, 2, 3]), 3)
        self.assertEqual(search([2, 2, 3, 3, 3]), 2)
        self.assertEqual(search([1, 2, 3, 4, 5]), 1)
        self.assertEqual(search([1, 1, 2, 3, 4]), 5)
        self.assertEqual(search([2, 2, 2, 3, 3]), 2)
        self.assertEqual(search([1, 1, 2, 2, 2]), 1)
        self.assertEqual(search([1, 2, 2, 2, 3]), 1)
        self.assertEqual(search([2, 2, 2, 3, 3]), 2)
        self.assertEqual(search([2, 3, 3, 3, 3]), 2)
        self.assertEqual(search([1, 2, 3, 3, 4]), 1)
        self.assertEqual(search([2, 3, 3, 4, 4]), 2)
        self.assertEqual(search([3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([4, 4, 4, 4, 4]), 4)
if __name__ == '__main__':
    unittest.main()

"""
"""
def search(arr):
    x = arr[-1]
    while arr:
        if x == arr[-1]:
            arr.pop()
        else:
            break