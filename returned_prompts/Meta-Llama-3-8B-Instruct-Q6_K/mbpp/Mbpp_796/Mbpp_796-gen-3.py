```
def return_sum(d):
    return sum(d.values())
```


Here is the explanation:
The problem is asking to write a function that takes a dictionary as an input and returns the sum of all its values. The function should sum up all the values in the dictionary.

The given unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` suggests that the function should return the sum of the values in the dictionary.

The solution is to use the built-in `sum` function in Python, which adds up all the items in an iterable (in this case, the values of the dictionary). The `values` method of a dictionary returns a view object that displays a list of all values in the dictionary. Therefore, we use `sum(d.values())` to get the sum of all values in the dictionary. This function will work for any dictionary, not just the one provided in the unit test. 





This solution assumes that the dictionary values are numbers. If the values are not numbers, you may need to modify the function to handle non-numeric values. For example, you could use a try-except block to catch any ValueError that occurs when trying to sum a non-numeric value. 

Here is an example of how you could modify the function to handle non-numeric values:

```
def return_sum(d):
    total = 0
    for value in d.values():
        try:
            total += value
        except TypeError:
            print(f"Skipping non-numeric value: {value}")
    return total
```





This modified function will skip any non-numeric values in the dictionary and continue to sum up the numeric values. It will also print a message for each non-numeric value it encounters.