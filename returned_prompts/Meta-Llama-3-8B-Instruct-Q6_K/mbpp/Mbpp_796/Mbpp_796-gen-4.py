```
def return_sum(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total
```


Explanation:
This function iterates over the values in the dictionary and adds them up. The `values()` method returns a view object that displays a list of all values in the dictionary. Then, it uses a for loop to iterate over these values and adds them to the `total` variable. Finally, it returns the `total`. The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` ensures that the function works correctly. 

This function does not check if the dictionary is empty. If you want to handle this case, you can add a check at the beginning of the function:
```
def return_sum(dictionary):
    if not dictionary:
        return 0
    total = 0
    for value in dictionary.values():
        total += value
    return total
``` 
This way, if the dictionary is empty, the function will return 0. 