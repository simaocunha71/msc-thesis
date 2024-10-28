```
def left_insertion(arr, val):
    if val < arr[0]:
        return 0
    for i in range(1, len(arr)):
        if val <= arr[i]:
            return i
    return len(arr)
```
The function takes a sorted array and a value as input, and returns the index where the value should be inserted to maintain the sorted order.

If the value is less than the first element in the array, it should be inserted at the beginning, so the function returns 0.

If the value is greater than or equal to the last element in the array, it should be inserted at the end, so the function returns the length of the array.

Otherwise, the function iterates through the array, comparing the value to each element, until it finds the first element that is greater than the value. At this point, the value should be inserted before this element, so the function returns the index of this element. 

For example, if the array is [1,2,4,5] and the value is 6, the function should return 4, because 6 should be inserted after 5 to maintain the sorted order. 

The unit test `assert left_insertion([1,2,4,5],6)==4` ensures that the function works correctly for this case. 

The time complexity of this function is O(n), where n is the length of the array, because it iterates through the array once. The space complexity is O(1), because it only uses a constant amount of space to store the index and the value. 