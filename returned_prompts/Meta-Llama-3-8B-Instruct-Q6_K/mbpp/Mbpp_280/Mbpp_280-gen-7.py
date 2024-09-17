```
def sequential_search(arr, element):
    for i, value in enumerate(arr):
        if value == element:
            return (True, i)
    return (False, -1)
```
The problem is asking you to create a function that searches for an element in an array and returns a tuple containing a boolean indicating whether the element is in the array and the index position of the element. If the element is not found, the index position should be -1.

The function should return (True, 3) if the element 31 is in the array [11,23,58,31,56,77,43,12,65,19]. This is because 31 is at index 3 in the array.

Here is a Python solution using the sequential search algorithm. This algorithm iterates over the array one element at a time, checking each element to see if it matches the target element. If a match is found, the function returns a tuple containing True and the index of the element. If the end of the array is reached without finding a match, the function returns a tuple containing False and -1.

The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` ensures that the function works correctly for the given input. The test checks that the function returns (True, 3) when the element 31 is in the array [11,23,58,31,56,77,43,12,65,19]. If the function does not return the expected result, the test will fail. This helps ensure that the function is working correctly.