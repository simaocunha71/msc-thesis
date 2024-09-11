Here's one way you can define the function:

```python
def find_Average_Of_Cube(n):
    return sum([i ** 3 for i in range(1, n + 1)]) / n
```

The function uses list comprehension to generate a list of cubes for the first `n` natural numbers, and then returns the average of that list.

The `sum()` function is a built-in Python function that computes the sum of all the items in an iterable.

The `range()` function returns an object that produces a sequence of integers, starting from 1 up to, but not including, `n + 1`.

To confirm that the function is working correctly, you can use the `assert` statement to check the output of the function for the example case you provided. Here's how you can do that:

```python
def test_find_Average_Of_Cube():
    assert find_Average_Of_Cube(2) == 4.5

test_find_Average_Of_Cube()
```

When you run this code, the `test_find_Average_Of_Cube()` function will be executed, and if the assertion is true (i.e., if the function does indeed return 4.5 for `n = 2`), then nothing will be printed. If the assertion is false, an error message will be printed, indicating the expected and actual results.

You can add more test cases to the `test_find_Average_Of_Cube()` function if you want to check the function for other values of `n`.

```python
def test_find_Average_Of_Cube():
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(5) == 20.625
    assert find_Average_Of_Cube(10) == 58.33333333333333

test_find_Average_Of_Cube()
```

In this updated version of the test function, we've added two more assertions to check