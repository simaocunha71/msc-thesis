You can use the built-in function sorted() along with a dictionary's items() method to sort a dictionary by its values. The sorted() function returns a new sorted list from the elements of any sequence. You can also use a lambda function to specify the sorting order.

Here is the solution:

```python
def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1], reverse=False)
```

This function sorts the dictionary items by their values in ascending order. If you want to sort in descending order, you can set the reverse parameter to True.

The unit test you provided:
```python
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
```
This test checks if the function sorts the dictionary items by their values in ascending order. The expected output is a list of tuples, where each tuple contains a key-value pair from the dictionary. The list is sorted in ascending order based on the values. The actual output of the function is compared with the expected output. If they are equal, the test passes; otherwise, it fails.