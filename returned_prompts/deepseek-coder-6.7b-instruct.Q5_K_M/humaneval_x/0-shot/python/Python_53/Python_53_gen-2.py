

def add(x: int, y: int):
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod()


"""
In the code above, the doctest.testmod() function is used to run the tests in the docstring. The function will return the number of tests executed and the number of tests that failed. If there are no failures, then all tests have passed.
"""

#test_add.py
import unittest
import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.add(2, 3), 5)
        self.assertEqual(add.add(5, 7), 12)
        self.assertEqual(add.add(-2, 3), 1)
        self.assertEqual(add.add(2.2, 3.3), 5.5)


if __name__ == '__main__':
    unittest.main()

"""
In the code above, we use Python’s built-in unittest module to create a simple test suite. We define a subclass of unittest.TestCase, TestAdd, that contains a method test_add(). This method calls the add function with different arguments and checks that the result is as expected.
"""

#test_add_doctest.py
import doctest
import add

doctest.testmod(add)

# If all the test cases pass, doctest will print a message indicating that all tests were successful. If any test case fails, doctest will print a message indicating the failure and the inputs that caused the failure.

#test_add_unittest.py
import unittest
import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.add(2, 3), 5)
        self.assertEqual(add.add(5, 7), 12)
        self.assertEqual(add.add(-2, 3), 1)
        self.assertEqual(add.add(2.2, 3.