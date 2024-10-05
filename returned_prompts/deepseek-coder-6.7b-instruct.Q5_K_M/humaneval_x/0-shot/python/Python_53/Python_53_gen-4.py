

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
    doctest.testmod(verbose=True)

#task_01_02/test_add.py
import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()

#task_01_02/test_add_v2.py
import pytest
from add import add


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (5, 7, 12),
    (-2, 3, 1),
    (-2, -3, -5),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

#task_01_02/test_add_v3.py
import doctest
from add import add


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(add))
    return tests


if __name__ == "__main__":
    doctest.testmod(verbose=True)

#task_01_03/test_add.py
import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7