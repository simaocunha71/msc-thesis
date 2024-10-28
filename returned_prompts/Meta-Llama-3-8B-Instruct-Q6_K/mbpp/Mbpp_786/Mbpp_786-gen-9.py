The problem is asking to create a function that finds the correct position to insert a given value into a sorted list so that the list remains sorted.

The unit test `assert right_insertion([1,2,4,5],6)==4` suggests that the function should return the index at which the value should be inserted to maintain the sorted order.

Here's a Python solution for the problem:
```
def right_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i] >= val:
            return i
    return len(lst)
```
This function iterates over the list and returns the index where the value should be inserted to maintain the sorted order. If the value is larger than all elements in the list, it returns the length of the list, indicating that the value should be appended to the end. 