
Here's a function that returns the median of the elements in the list l:

```python
def median(l: list):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        return l[len(l)//2]
```

This function first sorts the list `l` in ascending order using the `sort()` method. Then, it checks if the length of the list is even or odd using the modulo operator `%`. If the length is even, it calculates the median by taking the average of the two middle elements. If the length is odd, it simply returns the middle element as the median.

To test the function, you can use the `assertEqual` method from the `unittest` module to check if the function returns the correct median for the given inputs. For example:

```python
from unittest import TestCase

class TestMedian(TestCase):
    def test_median(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == "__main__":
    TestMedian().test_median()
```

This will run the tests and print the result to the console.

Note: The `assertEqual` method compares the actual result of the function with the expected result and raises an exception if they are not equal.

In the provided solution, the `median` function takes a list `l` as input and returns the median of the elements in that list. It first sorts the list in ascending order using the `sort()` method. Then, it checks if the length of the list is even or odd using the modulo operator `%`. If the length is even, it calculates the median by taking the average of the two middle elements. If the length is odd, it simply returns the middle element as the median.

To test the `median` function, the provided solution uses the `