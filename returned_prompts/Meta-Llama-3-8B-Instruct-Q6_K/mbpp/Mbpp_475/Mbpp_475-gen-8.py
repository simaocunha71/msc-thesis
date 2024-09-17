You can solve this problem by using the built-in sorted function in Python. The sorted function can sort a list of tuples based on the second element of each tuple. To sort a dictionary by value, you can convert the dictionary items into a list of tuples, where the first element of the tuple is the key and the second element is the value.

Here is the solution:
```
def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1], reverse=False)
```
This function takes a dictionary `counter` as input, converts it into a list of tuples using the `items` method, and then sorts the list of tuples based on the value (the second element of each tuple) using the `sorted` function. The `key` argument of the `sorted` function is a lambda function that specifies that the second element of each tuple should be used for sorting. The `reverse` argument is set to `False` by default, which means the list will be sorted in ascending order.

You can test this function using the following code:
```
print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
```
This should output:
```
[('Math', 81), ('Physics', 83), ('Chemistry', 87)]
```


