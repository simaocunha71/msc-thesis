The problem is asking to write a function that takes a list of tuples as input and returns a list containing the third element of each tuple.

The unit test `assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]` suggests that the third element of each tuple is the rear element, which is an integer.

Here is the solution:
```python
def rear_extract(tuples):
    return [t[2] for t in tuples]
```
This function uses a list comprehension to extract the third element (index 2) from each tuple in the input list and returns the resulting list. The unit test provided confirms that this function works as expected.