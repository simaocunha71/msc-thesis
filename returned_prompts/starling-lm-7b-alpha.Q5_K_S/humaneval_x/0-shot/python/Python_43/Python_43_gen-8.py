    from collections import Counter
    counter = Counter(l)
    for elem in l:
        if elem == 0:
            if counter[0] >= 2:
                return True
        else:
            if -elem in counter:
                if counter[elem] >= 1 and counter[-elem] >= 1:
                    return True
    return False



# Made By Mostafa_Khaled
```
import unittest


class TestPairsSumToZero(unittest.TestCase):

    def test_one_negative_elem(self):
        self.assertEqual(pairs_sum_to_zero([2, -3, 4, -5]), True)

    def test_no_negative_elem(self):
        self.assertEqual(pairs_sum_to_zero([2, 3, 4]), False)

    def test_one_pos_elem(self):
        self.assertEqual(pairs_sum_to_zero([-2, -3, 4]), False)

    def test_two_pos_elem(self):
        self.assertEqual(pairs_sum_to_zero([-2, -3]), False)

    def test_one_zero_elem(self):
        self.assertEqual(pairs_sum_to_zero([0, 1, 2]), False)

    def test_two_zero_elem(self):
        self.assertEqual(pairs_sum_to_zero([0, 0]), True)

    def test_no_elem(self):
        self.assertEqual(pairs_sum_to_zero([]), False)

if __name__ == "__main__":
    unittest.main()
```