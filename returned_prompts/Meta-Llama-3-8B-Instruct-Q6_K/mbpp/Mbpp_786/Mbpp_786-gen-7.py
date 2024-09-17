The problem is asking for a function that finds the correct position to insert a new element in a sorted list, so that the list remains sorted. This is often referred to as the "right insertion point".

Here's the solution:
```python
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```
This function iterates over the sorted list and returns the index where the value should be inserted to maintain the sorted order. If the value is greater than or equal to all elements in the list, it returns the length of the list, indicating that the value should be appended to the end of the list.

The unit test `assert right_insertion([1,2,4,5],6)==4` ensures that the function works correctly by checking that the right insertion point for the value 6 in the sorted list [1,2,4,5] is indeed 4. This is because 6 is greater than all elements in the list, so it should be inserted at the end. The function returns 4, which is the correct index.