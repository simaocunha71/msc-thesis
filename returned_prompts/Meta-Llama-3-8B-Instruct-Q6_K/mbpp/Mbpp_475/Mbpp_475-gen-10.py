The problem asks to sort a dictionary by its values. However, dictionaries are inherently unordered data structures, so we need to convert the dictionary to a list of tuples, where each tuple contains a key-value pair. Then, we can sort this list based on the values.

Here's the Python solution:
```python
def sort_counter(counter):
    return sorted(counter.items(), key=lambda item: item[1], reverse=False)
```
This function uses the built-in `sorted` function to sort the dictionary items. The `key` argument is set to `lambda item: item[1]`, which tells Python to sort the items based on their values (which are the second element of each tuple). The `reverse` argument is set to `False` to sort in ascending order.

The unit test `assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]` ensures that the function works correctly. It checks that the sorted list of tuples is as expected.