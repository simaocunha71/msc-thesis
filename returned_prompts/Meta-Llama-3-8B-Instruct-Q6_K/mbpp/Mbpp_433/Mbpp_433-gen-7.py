```
def check_greater(arr, num):
    return all(num > i for i in arr)
```
This function uses the built-in `all` function, which returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `num > i for i in arr` checks if `num` is greater than each element `i` in the array `arr`. If `num` is greater than all elements in the array, the function returns `True`; otherwise, it returns `False`. 

The unit test `assert check_greater([1, 2, 3, 4, 5], 4) == False` ensures that the function correctly identifies when the entered number is not greater than all elements in the array. 

For example, if you call `check_greater([1, 2, 3, 4, 5], 4)`, the function will return `False` because 4 is not greater than all elements in the array. If you call `check_greater([1, 2, 3, 4, 5], 6)`, the function will return `True` because 6 is greater than all elements in the array. 

This function can be used to check whether a given number is greater than all elements in a list. It is a simple and efficient solution that works for both positive and negative numbers. 

Note: The `all` function returns `True` if all elements are true; if at least one element is false, it returns `False`. The `any` function returns `True` if at least one element is true; if all elements are false, it returns `False`. These functions can be useful in a wide range of applications, from data processing to game development. 

In this specific problem, `all` is used to check if the given number is greater than all elements in the array. If the number is greater than all elements, the function returns `True`; otherwise, it returns `False`. This allows the function to correctly identify when the given number is not greater than all elements in the array. 

This solution is concise and easy to understand, making it a good choice for this problem. It also works for both positive and negative numbers, and it is efficient because it only needs to iterate over the array once. 

Overall, this solution is a good example of how to use the `all` function to check if a given number is greater than all elements