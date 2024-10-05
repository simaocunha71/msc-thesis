

    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#tests.py
import unittest
from pairs_sum_to_zero import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):
    def test_pairs_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()

#run_tests.py
import unittest
from tests import TestPairsSumToZero

if __name__ == '__main__':
    unittest.main()

#test_pairs_sum_to_zero.py
import unittest
from pairs_sum_to_zero import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):
    def test_pairs_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3