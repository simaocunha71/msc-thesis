The problem is asking you to create a function that takes a list as an input and returns the sum of all the elements in the list. The list can contain integers, lists, or a mix of both. If the list contains another list, the function should recursively flatten the list and then sum all the elements.

Here's a Python solution for the problem:
```
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total
```
This function works by iterating over each element in the list. If the element is a list, the function calls itself with that list as the argument. If the element is not a list, the function adds it to the total sum. The function continues this process until it has processed all the elements in the list, at which point it returns the total sum. The unit test `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21` ensures that the function works correctly. 