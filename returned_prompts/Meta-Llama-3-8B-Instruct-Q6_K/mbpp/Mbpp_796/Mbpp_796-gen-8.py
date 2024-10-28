```
def return_sum(dictionary):
    return sum(dictionary.values())
```



Explanation:

*   The problem is asking to create a function that takes a dictionary as an input and returns the sum of all its values.
*   The dictionary is a collection of key-value pairs, where each key is a string and each value is a number.
*   The unit test provided suggests that the function should return the sum of all values in the dictionary. For example, if the input is `{'a': 100, 'b':200, 'c':300}`, the function should return `600`.
*   To solve this problem, we can use the built-in `sum` function in Python, which calculates the sum of all items in an iterable (like a list or a dictionary).
*   We can pass the dictionary to the `sum` function using the `values` method, which returns a view object that displays a list of all values in the dictionary.
*   The `sum` function will then add up all these values and return the result.

Here's the solution:

```
def return_sum(dictionary):
    return sum(dictionary.values())
```

This function takes a dictionary as an input, uses the `values` method to get a list of all values in the dictionary, and then returns the sum of these values using the `sum` function. The unit test provided ensures that this function works correctly.