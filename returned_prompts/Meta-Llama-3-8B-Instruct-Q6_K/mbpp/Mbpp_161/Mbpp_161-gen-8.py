```
def remove_elements(lst, lst2):
    return [i for i in lst if i not in lst2]
```



Explanation:
The problem is asking to create a function that takes two lists as input, and returns a new list that contains all the elements from the first list that are not present in the second list.

The unit test provided is `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]`.

The solution to this problem is a list comprehension that iterates over the elements in the first list, and includes the element in the new list only if it is not present in the second list.

Here is the Python code for the solution:
```
def remove_elements(lst, lst2):
    return [i for i in lst if i not in lst2]
```
This function uses a list comprehension to create a new list that contains all the elements from the first list that are not present in the second list. The `if` condition `i not in lst2` is used to filter out the elements that are present in the second list. The resulting list is then returned.