Here's a Python function that can find the element that appears only once in a sorted array:

```python
def search(arr):
    left, right = 0, len(arr) - 1
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

This function uses a binary search approach to find the element that appears only once in the array. It starts with a left pointer at the beginning of the array and a right pointer at the end of the array. It repeatedly compares the middle element with the elements at the left and right pointers. If the middle element is equal to the left element, it moves the left pointer to the right. If the middle element is equal to the right element, it moves the right pointer to the left. If the middle element is neither equal to the left nor right element, it returns the middle element. This process continues until the left and right pointers meet, at which point it returns the element at the left pointer, which is the element that appears only once in the array.

You can test this function with the provided assert statement to verify its correctness:

```python
assert search([1,1,2,2,3]) == 3
```

This assert statement checks if the function correctly returns the element that appears only once in the array [1,1,2,2,3]. In this case, the function should return 3, which is the expected result.

By using this function, you can easily find the element that appears only once in a sorted array in Python.

```python
def search(arr):
    left, right = 0, len(arr) - 1
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

This function efficiently solves the problem of finding the element