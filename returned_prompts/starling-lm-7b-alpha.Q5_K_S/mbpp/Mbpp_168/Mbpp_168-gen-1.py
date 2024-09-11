def frequency(lst, target):
    """
    Count the number of occurrences of a number in a given list.
    """

    # Initialize the count to 0
    count = 0
    # Iterate through the list and compare each element to the target
    for item in lst:
        if item == target:
            count += 1
    # Return the count
    return count


# Test the function
print(frequency([1,2,3], 4)) # 0
print(frequency([1,2,3,4], 3)) # 2
print(frequency([1,1,2,3,4], 1)) # 2
print(frequency([1,2,3,4,3,3,3,3], 3)) # 4

# Run the unit test
import unittest

class TestFrequency(unittest.TestCase):
    def test_frequency(self):
        self.assertEqual(frequency([1,2,3], 4), 0)
        self.assertEqual(frequency([1,2,3,4], 3), 2)
        self.assertEqual(frequency([1,1,2,3,4], 1), 2)
        self.assertEqual(frequency([1,2,3,4,3,3,3,3], 3), 4)

    def test_frequency_edge_cases(self):
        self.assertEqual(frequency([], 3), 0)
        self.assertEqual(frequency([3], 3), 1)
        self.assertEqual(frequency([3,3], 3), 2)

if __name__ == '__main__':
    unittest.main()

# End of file

"""
Write a function to count the number of occurrences of a number in a given list.

Test cases:

frequency([1,2,3], 4) == 0
frequency([1,2,3,4], 3) == 2
frequency([1,1,2,3,4], 1) == 2
frequency([1,2,3,4,3,3,3,3], 3) == 4

Test the function

Run