

def sort_even(l: list):
    # Store values at even indices
    evens = [l[i] for i in range(0, len(l), 2)]
    # Sort the even values
    evens.sort()
    # Create a new list with the sorted even values and the original odd values
    new_l = [evens.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
    return new_l


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

#test_sort_even.py
import unittest
import sort_even


class TestSortEven(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even.sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even.sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
        self.assertEqual(sort_even.sort_even([10, 5, 2, 7, 6, 8]), [2, 5, 6, 7, 10, 8])


if __name__ == "__main__":
    unittest.main()