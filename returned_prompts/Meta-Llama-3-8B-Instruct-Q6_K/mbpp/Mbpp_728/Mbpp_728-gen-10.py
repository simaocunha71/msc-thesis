```
def sum_list(a, b):
    return [x+y for x,y in zip(a,b)]
```
The function `sum_list` takes two lists `a` and `b` as input and returns a new list where each element is the sum of the corresponding elements in `a` and `b`. The `zip` function is used to iterate over the two lists in parallel, and a list comprehension is used to create the new list. The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` ensures that the function works correctly. 

This problem is an example of a map operation, where each element of the input lists is transformed into a new value. The `zip` function is used to pair the elements of the two lists, and the list comprehension is used to create the new list. 

The time complexity of this function is O(n), where n is the length of the input lists, because it needs to iterate over each element of the lists once. The space complexity is also O(n), because it needs to create a new list of the same length as the input lists. 







