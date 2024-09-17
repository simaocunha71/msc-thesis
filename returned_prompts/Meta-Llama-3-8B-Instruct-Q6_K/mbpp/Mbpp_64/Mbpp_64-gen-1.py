You can use the built-in sorted function in Python, which can be used to sort a list of tuples based on a specific key. In this case, the key is the second element of each tuple.

Here is the function:

```python
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])
```

This function takes a list of tuples as input, where each tuple contains a subject and its corresponding mark. The sorted function is then used to sort this list of tuples based on the second element of each tuple (i.e., the mark). The lambda function is used as the key for the sorted function, which tells it to use the second element of each tuple as the sorting key.

The unit test provided in the problem ensures that this function works correctly. It checks that the function returns a list of tuples sorted by the second element of each tuple. The expected output for the given input is `[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]`, which is the sorted version of the input list. This test ensures that the function is working correctly.