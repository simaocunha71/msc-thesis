```
def extract_singly(input):
    # flatten the list of lists
    flatten_list = [num for sublist in input for num in sublist]
    # convert the flattened list to set
    flat_set = set(flatten_list)
    # return the set
    return flat_set
```

Explanation:

This function `extract_singly` takes a list of lists as input and flattens it into a single set of numbers. It achieves this by first using a list comprehension to create a new list that contains all the numbers from each sublist in the input list. Then, it converts this flattened list into a set using the built-in `set` function. Finally, it returns the set of unique numbers.

The `set` function is used to remove any duplicate numbers from the list, ensuring that the resulting set only contains unique elements. The assert statement is used to test the function and check if the set of numbers returned by the function matches the expected result.

Overall, this function provides a concise and efficient solution to flatten a list of lists into a single set of unique numbers.

Here is the Python code that implements this function:

```python
def extract_singly(input):
    # flatten the list of lists
    flatten_list = [num for sublist in input for num in sublist]
    # convert the flattened list to set
    flat_set = set(flatten_list)
    # return the set
    return flat_set
```

And here is the assert statement that tests the function:

```python
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
```

When you run this code, it will print `True` if the assert statement passes, indicating that the function correctly flattens the list of lists into a single set of unique numbers.

Here is the Python code that tests the function:

```python
def test_extract_singly():
    assert set(extract_singly([(3, 4, 5), (4