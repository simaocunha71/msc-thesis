```
def smallest_num(lst):
    return min(lst)
```
The problem asks you to write a function that finds the smallest number in a given list. You can use the built-in `min()` function in Python to achieve this. The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments. 

For example, if you have a list `[10, 20, 1, 45, 99]`, the `min()` function will return `1`, which is the smallest number in the list. 

The unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1` also confirms this, as it checks if the function returns `1` when given the list `[10, 20, 1, 45, 99]`. 

Here is the Python function that solves the problem:

```
def smallest_num(lst):
    return min(lst)
```

This function takes a list `lst` as input and returns the smallest number in the list. You can use this function to find the smallest number in any list. 

For example, if you have a list of numbers and you want to find the smallest number, you can use the function like this:

```
numbers = [10, 20, 1, 45, 99]
smallest = smallest_num(numbers)
print(smallest)  # Output: 1
``` 







