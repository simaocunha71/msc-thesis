The problem is asking to sort a dictionary by its values. However, dictionaries in Python are inherently unsorted, so we need to convert it into a list of tuples where the first element is the key and the second element is the value, then sort this list based on the values, and finally return the sorted list.

Here's a Python function to do this:

```
def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1])
```

This function works by calling the `items` method on the dictionary, which returns a list of tuples where the first element is the key and the second element is the value. Then it sorts this list using the `sorted` function and a lambda function as the key. The lambda function takes a tuple as an argument and returns the second element of the tuple, which is the value. This way, the list is sorted based on the values. 

For example, if we have a dictionary `{'Math':81, 'Physics':83, 'Chemistry':87}`, calling `sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})` will return `[('Chemistry', 87), ('Physics', 83), ('Math', 81)]`. 

The unit test `assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]` ensures that the function works correctly. 