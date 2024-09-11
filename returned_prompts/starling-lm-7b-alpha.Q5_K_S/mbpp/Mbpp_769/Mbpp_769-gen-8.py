Here is a simple Python function to get the difference between two lists:

```python
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]
```

And a unit test to ensure the function works correctly:

```python
def test_Diff():
    assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
    print('All tests passed.')

if __name__ == "__main__":
    test_Diff()
```

To run this code, copy it to a Python file (for example, `diff_test.py`) and run the Python file with the command `python diff_test.py`.

```python
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]
```

This function uses list comprehension to create a new list that only contains elements from `list1` that are not in `list2`. The `if i not in list2` condition filters out any elements in `list1` that are also in `list2`.

```python
def test_Diff():
    assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
    print('All tests passed.')
```

This unit test calls the `Diff` function with a sample input and asserts that the result is the expected output. If the function produces the correct result, the test passes and the message "All tests passed." is printed.

To run the tests, you can use a tool like `unittest` or simply run the script with the Python interpreter.

```python
if __name__ == "__main__":
    test_Diff()
```

This line ensures that the `test_Diff` function is only run if the script is executed directly (not imported as a module).

Overall