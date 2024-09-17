The problem is asking to write a function that finds the right insertion point for a specified value in a sorted list. This means finding the index where the value should be inserted to maintain the sorted order.

The unit test `assert right_insertion([1,2,4,5],6)==4` suggests that the function should return the index where the value 6 should be inserted in the sorted list [1,2,4,5] to maintain the sorted order.

Here's a Python solution for the problem:
```
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```
This function iterates over the sorted list and returns the index where the value should be inserted. If the value is greater than all elements in the list, the function returns the length of the list, indicating that the value should be appended at the end.  # 5:30 PM, 28/03/2021
```python
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```
This function iterates over the sorted list and returns the index where the value should be inserted. If the value is greater than all elements in the list, the function returns the length of the list, indicating that the value should be appended at the end.  # 5:30 PM, 28/03/2021
```python
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```
This function iterates over the sorted list and returns the index where the value should be inserted. If the value is greater than all elements in the list, the function returns the length of the list, indicating that the value should be appended at the end.  # 5:30 PM, 28/03/2021
```python
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```
This function iterates over the sorted list and returns the index where the value should be inserted. If the value is greater than all elements in the list, the function returns the length of the list