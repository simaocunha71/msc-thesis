```python
def find_first_occurrence(array, target):
    array_length = len(array)
    for i in range(array_length):
        if array[i] == target:
            return i
    return -1
```

Explanation:
The function `find_first_occurrence` takes two parameters: `array`, which is the sorted array, and `target`, which is the number we are looking for. It returns the index of the first occurrence of `target` in `array` or -1 if `target` is not found.

The function uses a for loop to iterate through each element in `array`. Inside the loop, it checks if the current element is equal to `target`. If it is, the function returns the index of the current element. If no match is found after iterating through the entire array, the function returns -1.

In the given test case, the function is called with the array `[2, 5, 5, 5, 6, 6, 8, 9, 9, 9]` and the target number `5`. The function correctly identifies that the first occurrence of `5` is at index `1`, and returns this value.

Note: This solution assumes that the array is sorted in ascending order. If the array is not sorted, a different approach would be needed to find the index of the first occurrence of a number.

```python
# Testing the function
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # Output: 1
```

This code tests the `find_first_occurrence` function with the provided test case and prints the result, which should be `1`.

```python
# Testing with a different array
print(find_first_occurrence([3, 5, 7, 9, 11], 7))  # Output: 2
```

This code tests the `find_first_occurrence` function with a different array and prints the result, which should be `2`.

```python
# Testing with a number not in