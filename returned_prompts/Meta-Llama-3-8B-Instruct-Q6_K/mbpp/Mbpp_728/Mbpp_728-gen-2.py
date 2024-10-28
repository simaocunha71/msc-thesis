```
def sum_list(a, b):
    return [x+y for x, y in zip(a, b)]
```


The function takes two lists `a` and `b` as input and returns a new list where each element is the sum of the corresponding elements in `a` and `b`. The `zip` function is used to iterate over the two lists in parallel, and the list comprehension is used to create the new list. 

The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` ensures that the function works correctly for the given input. 

This problem can also be solved using a for loop:
```
def sum_list(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x+y)
    return result
```


This function uses the `zip` function to iterate over the two lists in parallel, and the `append` method to add each sum to the result list. The result list is then returned. 

This problem can also be solved using list comprehension:
```
def sum_list(a, b):
    return [sum(pair) for pair in zip(a, b)]
```


This function uses the `zip` function to iterate over the two lists in parallel, and the list comprehension to create a new list where each element is the sum of the corresponding elements in `a` and `b`. 

All three solutions are equivalent and will produce the same output for the given input. 

The time complexity of this function is O(n), where n is the length of the input lists. This is because the function iterates over the input lists once. The space complexity is also O(n), as the function creates a new list of the same length as the input lists. 