def square_nums(nums):
    return [num ** 2 for num in nums]



def square_nums(nums):
    return [num ** 2 for num in nums]


# Testing
from __future__ import division
import unittest

class TestSquareNums(unittest.TestCase):

    def test_square_nums(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

        self.assertEqual(square_nums([]), [])
        self.assertEqual(square_nums([0]), [0])
        self.assertEqual(square_nums([1]), [1])
        self.assertEqual(square_nums([-1]), [1])
        self.assertEqual(square_nums([10.5]), [10.25])
        self.assertEqual(square_nums([0.0]), [0.0])

if __name__ == '__main__':
    unittest.main()



"""
Test Cases:
square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
square_nums([])
square_nums([0])
square_nums([1])
square_nums([-1])
square_nums([10.5])
square_nums([0.0])
"""



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

```

``