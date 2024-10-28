```
def extract_singly(lst):
    return set(num for sublist in lst for num in sublist)
```





The problem is asking to create a function that takes a list of lists as input and returns a set of unique numbers. 

The given unit test suggests that the input list contains tuples, not lists. Therefore, the function should extract the numbers from the tuples and put them into a set.

Here's a Python solution using list comprehension and set:

```
def extract_singly(lst):
    return set(num for sublist in lst for num in sublist)
```

This function uses a list comprehension to iterate over each sublist in the input list, and then over each element in the sublist. It converts the result into a set, which automatically removes any duplicate elements. The resulting set is then returned.