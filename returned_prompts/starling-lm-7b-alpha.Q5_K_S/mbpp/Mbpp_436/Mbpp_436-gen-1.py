```
def neg_nos(list):
    return [i for i in list if i < 0]
```

Explanation:
This function takes in a list of integers and uses list comprehension to return a new list containing all the negative numbers from the original list. 

Here's how it works:

- The function `neg_nos` takes a list as an argument.
- Inside the function, a list comprehension is used to iterate over each element `i` in the input list.
- The condition `i < 0` is used to filter out the negative numbers from the original list.
- The filtered negative numbers are then returned as a new list.

The `assert` statement at the beginning of the code is used to verify that the function is working correctly. It checks if the function correctly returns the expected output for the given input `[-1,4,5,-6]`, which should be `[-1,-6]`. If the assertion fails, an `AssertionError` will be raised, indicating that there is an error in the function's implementation.

You can use this function by calling it with a list of integers as an argument, like this:
```python
print(neg_nos([-1,4,5,-6]))  # Output: [-1, -6]
```

This will print the list of negative numbers from the given input list.

Note: The `assert` statement is a debugging tool in Python that is used to catch errors and ensure that certain conditions are met. It is not necessary to include an `assert` statement in a function if you are not using it for debugging purposes.

Additionally, please note that the code provided is written in Python, not JavaScript.

In JavaScript, you can achieve the same functionality using the following code:
```javascript
function getNegativeNumbers(list) {
    return list.filter(function(i) { return i < 0; });
}
```
This function uses the `filter` method on the input list to iterate over each element `i` and return a new array containing only the negative numbers.

To use this function, you can call it with a list of numbers as an argument, like this:
```javascript
var negativeNumbers = getNegative