You can use a list comprehension with the index -1 to extract the last element of each tuple.

Here is the solution:
```python
def rear_extract(tuples):
    return [t[-1] for t in tuples]
```
This function uses a list comprehension to iterate over each tuple in the input list. For each tuple, it extracts the last element using the index -1 and adds it to the output list. The resulting list contains the last element of each tuple.

The unit test `assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]` ensures that the function works correctly. It checks that the output of the function is equal to the expected result. If the output is not equal to the expected result, the test fails and the function is considered incorrect.