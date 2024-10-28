```
def return_sum(dictionary):
    return sum(dictionary.values())
```


Explanation:
The problem is asking to write a function that takes a dictionary as input and returns the sum of all its values. 

The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` suggests that the function should return the sum of all values in the dictionary. 

The function `return_sum` can use the built-in `sum` function along with the `values` method of the dictionary to achieve this. The `values` method returns a view object that displays a list of all values in the dictionary. The `sum` function then adds up all these values and returns the result. 

For example, if the input dictionary is `{'a': 100, 'b':200, 'c':300}`, the function will return `100 + 200 + 300 = 600`.  This is confirmed by the unit test. 