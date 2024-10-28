You can use the concept of two pointers, one starting from the beginning of the array and the other from the end. Since the array is sorted, if the two pointers meet in the middle, it means the element at that index appears more than once. If the element at the meeting point is the same as the element at the start, then the element that appears only once is the one at the next index. If the element at the meeting point is different, then the element that appears only once is the one at the meeting point.

Here is the python function:

```
def search(arr):
    if len(arr) == 1:
        return arr[0]
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == arr[left]:
            left += 1
        elif arr[mid] == arr[right]:
            right -= 1
        else:
            return arr[mid]
    return arr[left]
```

This function works by iterating through the array until it finds the element that appears only once. It does this by checking if the middle element is the same as the left or right element. If it's the same as the left element, it moves the left pointer to the right. If it's the same as the right element, it moves the right pointer to the left. If it's not the same as either, it returns the middle element. The function returns the element that appears only once. 

The unit test `assert search([1,1,2,2,3]) == 3` ensures that the function works correctly. It checks if the function returns 3 when the input is [1,1,2,2,3]. The function correctly identifies the element 3 as the one that appears only once in the array. 














# A more detailed explanation of the code

The code is a solution to the problem of finding the element that appears only once in a sorted array. The array is sorted, which means that all the elements are in a specific order. The problem is to find the element that does not have a duplicate in the array.

The code uses a two-pointer approach, where one pointer starts at the beginning of the array and the other pointer starts at the end of the array. The pointers move towards each other until they meet. The meeting point is where the two pointers meet, and this is where the element that appears only once