```
def recursive_list_sum(lst):
    sum = 0
    for item in lst:
        if isinstance(item, list):
            sum += recursive_list_sum(item)
        else:
            sum += item
    return sum
```
The problem is asking to write a function that takes a list as an input and returns the sum of all its elements. The list can contain both integers and other lists. The function should recursively iterate through the list and sum all its elements. If the list contains other lists, the function should also recursively sum their elements.

The unit test `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21` helps to clarify the problem by showing an example of a list that contains both integers and other lists, and the expected sum.

Here is the solution:
```
def recursive_list_sum(lst):
    sum = 0
    for item in lst:
        if isinstance(item, list):
            sum += recursive_list_sum(item)
        else:
            sum += item
    return sum
```
This function works by iterating through the input list and checking if each item is a list. If it is, the function calls itself with that list as the input, effectively recursively summing its elements. If the item is not a list, it is simply added to the sum. The function returns the total sum of all elements in the list and its nested lists.