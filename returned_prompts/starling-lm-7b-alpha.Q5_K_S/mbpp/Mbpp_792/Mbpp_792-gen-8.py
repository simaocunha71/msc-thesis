def count_list(l):
    count = 0
    for i in l:
        if isinstance(i, list):
            count += 1
    return count


def test_count_list():
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4


test_count_list()

"""
This function uses a for loop to iterate through the given list, and within the loop it checks if the element is of type list using the isinstance function. If the element is a list, the count variable is incremented by one. Finally, the function returns the count.
"""

"""
Test cases:
- Input: [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
  Expected Output: 4
"""

```
import unittest

class TestCountList(unittest.TestCase):
    def test_count_list(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()
```

In the provided solution, the count_list function is tested using the unittest module. The test_count_list class inherits from unittest.TestCase and defines a test_count_list method. Within this method, the count_list function is called with a sample input and the expected output is compared using the self.assertEqual method. The unittest.main() function is used to run the tests.

To run the tests, you can save the code in a file named test_count_list.py and execute the command "python -m unittest test_count_list" in your command prompt or terminal. This will run the tests and display the results, indicating whether the test passed or failed.
```

```

```

```

```

```

```

```

```

```

```

```

```