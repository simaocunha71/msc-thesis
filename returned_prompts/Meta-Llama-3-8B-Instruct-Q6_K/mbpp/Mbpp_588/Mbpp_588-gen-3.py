```
def big_diff(lst):
    return max(lst) - min(lst)
```


The function `big_diff` takes a list `lst` as an argument and returns the difference between the largest and smallest value in the list. The `max` function returns the largest value in the list, and the `min` function returns the smallest value. The difference between these two values is calculated by subtracting the smallest value from the largest value. For example, if the list is `[1,2,3,4]`, the function will return `4-1 = 3`. This is confirmed by the unit test `assert big_diff([1,2,3,4]) == 3`. 

Please note that the function does not handle empty lists, if the list is empty, it will throw an error. If you want to handle this case, you can add a condition to check if the list is empty, and return a specific value or throw an error accordingly. For example:

```
def big_diff(lst):
    if len(lst) == 0:
        return "List is empty"
    return max(lst) - min(lst)
```


This will return the string "List is empty" if the list is empty, instead of throwing an error. You can modify this to fit your specific requirements. 