```
def return_sum(dict):
    sum = 0
    for key in dict:
        sum += dict[key]
    return sum
```


The function `return_sum` takes a dictionary as an argument and returns the sum of all its items. It does this by iterating over each key in the dictionary, adding the corresponding value to a running total, and finally returning the total. The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` ensures that the function works correctly.