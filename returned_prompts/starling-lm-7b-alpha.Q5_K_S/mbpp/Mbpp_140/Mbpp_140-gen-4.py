"""
Here's one possible solution to the problem:

```python
def extract_singly(t):
    result = []
    for sublist in t:
        for elem in sublist:
            result.append(elem)
    return result
```

To test the function, we can use the `assert` keyword to compare the expected output (`set([3, 4, 5, 7, 1])`) with the actual output of the function. Here's the test case:

```python
def test_extract_singly():
    assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])

test_extract_singly()
```

The `test_extract_singly` function calls the `extract_singly` function with a sample input list and asserts that the returned set matches the expected set. If the assertion is true, no error will be raised and the test will pass. Otherwise, an `AssertionError` will be raised, indicating that the test has failed.

This approach allows us to test the functionality of the `extract_singly` function and ensure that it correctly flattens the input list of lists into a single set of numbers.
"""

def extract_singly(t):
    result = []
    for sublist in t:
        for elem in sublist:
            result.append(elem)
    return result

def test_extract_singly():
    assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])

test_extract_singly()


```
```
```