```
def is_majority(arr, n, element):
    if n <= 0:
        return False
    if n == 1:
        return arr[0] == element
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            left, right = 0, mid
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return left < n and arr[left] == element
```
This function uses binary search to find the element in the array. It keeps track of the left and right pointers and updates them based on whether the middle element is equal to the target element. If the element is found, it then checks if the element is the majority element by checking if it's present at the left pointer. If the left pointer is less than the length of the array and the element at the left pointer is equal to the target element, then the element is the majority element. Otherwise, it returns False. The time complexity of this function is O(log n) and the space complexity is O(1). 