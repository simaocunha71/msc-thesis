

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#tests.py
import unittest
from main import add


class TestAdd(unittest.TestCase):
    """
    Test the add function from the main.py
    """
    def test_add(self):
        """
        Test that it can add numbers
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


if __name__ == "__main__":
    unittest.main()

#tests_doctest.py
import doctest
from main import add


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(add))
    return tests


if __name__ == "__main__":
    doctest.testmod(verbose=True)