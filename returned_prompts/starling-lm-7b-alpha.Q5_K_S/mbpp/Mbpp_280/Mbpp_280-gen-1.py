```
def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)
```

Here is a solution that uses a for loop to iterate through the array. It checks if the element at each index is equal to the target element. If it is, it returns a tuple containing True and the index of the element. If it is not, it continues to the next element in the array. If the for loop finishes without finding the target element, it returns a tuple containing False and -1, indicating that the element was not found.

To test the function, you can use the `assert` statement to check if the function returns the correct result for the provided example. In this case, the function should return `(True, 3)` because the element `31` is located at index `3` in the array `[11,23,58,31,56,77,43,12,65,19]`.

You can call the function with different inputs to test its behavior. For example, you can test if the function correctly returns `(False, -1)` when the target element is not present in the array.

Overall, this solution provides a simple and efficient way to search for an element in an array using a sequential search algorithm.

Here are some additional notes on the solution:

- The function `sequential_search` takes in two parameters: `array` and `element`. `array` represents the array to be searched, and `element` represents the element to be found.
- The function uses a `for` loop to iterate through each element in the `array`. It compares each element with the `element` using the `==` operator.
- If the element is found, the function returns a tuple containing `True` (indicating that the element is in the array) and the index position of the element.
- If the element is not found, the function returns a tuple containing `False` (indicating that the element is not in the array) and `-1` (indicating the absence of the element).
- The provided assert statement checks if the function correctly returns `(True, 3)` for the