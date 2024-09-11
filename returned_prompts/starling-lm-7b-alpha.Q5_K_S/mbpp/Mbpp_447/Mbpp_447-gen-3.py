Here's a Python function that solves the problem:

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

This function uses a list comprehension to create a new list. For each element in the input list, it raises the element to the third power (cubes it) using the exponentiation operator `**`. The resulting cubes are stored in a new list which is returned by the function.

You can use this function like this:

```python
print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

This will print the cubes of the individual elements in the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, which are `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`.

```python
import unittest

class TestCubeNums(unittest.TestCase):
    def test_cube_nums(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()
```

This is a unit test that checks if the `cube_nums` function returns the expected result. When you run this script, it will execute the test and print `.` if the test passed or an error message if the test failed.

```