def left_insertion(list, item):
    i = 0
    while i < len(list) and item > list[i]:
        i += 1
    return i

# Test
assert left_insertion([1,2,4,5],6) == 4

"""
Explanation: 
This function works by traversing the given list and checking if the item is greater than the current element. If the current element is less than the item, the index is incremented. This process continues until the end of the list or until the item is no longer greater than the current element. The function then returns the index where the item should be inserted to maintain the sorted order.
"""

"""
Here's a step-by-step explanation of how the function works:

1. Initialize a variable 'i' to 0, which will be used as the index for traversing the list.
2. Enter a while loop that will continue until 'i' is equal to the length of the list or until the item is no longer greater than the current element in the list.
3. Inside the while loop, increment 'i' by 1 as long as the item is greater than the current element in the list. This ensures that the index 'i' will always point to the correct position where the item should be inserted.
4. Once the while loop ends, the function returns the value of 'i', which represents the left insertion point for the specified value in sorted order.
5. The function also includes an assert statement to verify that the function is working correctly. In this case, the assert statement checks if the left insertion point for the value 6 in the list [1,2,4,5] is indeed 4.
"""

"""
To use this function, you can simply pass in a sorted list and the value you want to insert. The function will return the left insertion point for that value in the sorted order. For example, if you call left_insertion([1,2,4,5],6), the function will return 4, indicating that the value 6 should be inserted at index 4 in the list to maintain the sorted order."""

```python
def left_insertion(list, item):
    i = 0
    while i < len(list) and item > list[i]: