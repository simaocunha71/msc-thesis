```
def return_sum(d):
    return sum(d.values())
```
This function takes a dictionary as an argument and returns the sum of all its values. The `values()` method of a dictionary returns a view object that displays a list of all values in the dictionary. The `sum()` function then adds up all these values. 

The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` ensures that the function returns the expected result for a given dictionary. 

For example, if you call `return_sum({'a': 100, 'b':200, 'c':300})`, it should return `600` which is the sum of the values in the dictionary. 