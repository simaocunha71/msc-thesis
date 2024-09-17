```
def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=False)
```


This problem is about sorting a dictionary by its values. The dictionary is a simple counter where keys are subject names and values are corresponding scores.

The unit test provided suggests that the function should return a list of tuples, where each tuple contains a subject name and its corresponding score, sorted in ascending order of scores.

The solution uses the built-in `sorted` function in Python, which sorts a list. The `key` argument of the `sorted` function is a function that takes a list element and returns a value that will be used for sorting purposes. In this case, the `key` function is a lambda function that returns the value of each item in the dictionary.

The `sorted` function returns a new sorted list from the elements of any sequence. In this case, the sequence is the dictionary's items (i.e., key-value pairs). The `reverse=False` argument means that the sorting is done in ascending order.

For example, if we have a dictionary `{'Math':81, 'Physics':83, 'Chemistry':87}`, the `sort_counter` function will return `[('Math', 81), ('Physics', 83), ('Chemistry', 87)]`, which is the dictionary sorted by its values in ascending order.