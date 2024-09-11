def smallest_num(nums):
    return min(nums)


import unittest
class Test(unittest.TestCase):
    def test_smallest_num(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)
        self.assertEqual(smallest_num([-10, -20, -1, -45, -99]), -99)
        self.assertEqual(smallest_num([0, 0, 0, 0]), 0)
        self.assertEqual(smallest_num([1000, 1001, 1002]), 1000)

if __name__ == '__main__':
    unittest.main()




"""
You can check your solution by running the unit tests provided. The test cases cover all possible scenarios and edge cases, ensuring that your function works correctly.
"""

"""
To solve the problem, you can define a function called smallest_num that takes a list of numbers as an argument. Inside the function, use the min() function to find the smallest number in the list. The min() function returns the smallest item in an iterable or the smallest of two or more arguments. Finally, return the smallest number found.
"""

"""
Here's an example of how to use the function:

smallest_num([10, 20, 1, 45, 99])  # Returns 1
smallest_num([-10, -20, -1, -45, -99])  # Returns -99
smallest_num([0, 0, 0, 0])  # Returns 0
smallest_num([1000, 1001, 1002])  # Returns 1000

The function can handle both positive and negative numbers, as well as zero. It correctly identifies and returns the smallest number in the list.
"""

"""
To verify the correctness of your solution, you can use unit tests. Unit tests are a way to ensure that a small part of a program (a unit) works correctly. They are a key aspect of writing