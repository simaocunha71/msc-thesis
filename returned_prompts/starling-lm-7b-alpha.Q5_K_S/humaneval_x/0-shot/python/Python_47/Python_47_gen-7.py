
Here are some tests you can use to check whether your implementation is correct:

```python
from random import sample
from statistics import median as stat_median

def test_median():
    # Test on a few small cases
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([0, 1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6]) == 3.0
    assert median([7, 8, 9, 10]) == 8.5

    # Test on some larger cases
    for _ in range(100):
        l = sample(range(1000), 5)
        assert median(l) == stat_median(l)

    print("All tests passed.")

test_median()
```

The above tests include a few small cases that your function should handle easily, and a number of larger cases that test the ability of your function to work with larger inputs.

The `sample` function is used to generate a small list of random integers from a larger range. This helps test your function on inputs that it might not have seen during development.

The `stat_median` function from the `statistics` module is used as a reference implementation of median. This helps ensure that your function is correct, as it is a well-tested and commonly-used implementation.

The `assert` statements in the tests compare the output of your `median` function with the output of `stat_median`. If the two outputs are not equal for any of the test cases, the test will fail and an error message will be printed.

If all of the test cases pass, the message "All tests passed." will be printed.

The tests should be run in an interactive Python shell or REPL, such as IDLE or Jupyter Notebook. They cannot be run directly from a Python file.

To run the tests, copy the code into an interactive Python shell or REPL,