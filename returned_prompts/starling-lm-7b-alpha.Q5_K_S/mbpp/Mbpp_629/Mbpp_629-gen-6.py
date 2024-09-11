```python
def Split(arr):
    return [num for num in arr if num % 2 == 0]
```

Explanation:
This function uses a list comprehension to create a new list containing only the even numbers from the input list.

The `Split` function takes in a list of numbers as the `arr` parameter. It uses a list comprehension to iterate over each number in the input list and checks if the number is divisible by 2 (i.e., an even number) by using the modulo operator (`%`). If the number is even, it is added to the new list.

The list comprehension syntax `[num for num in arr if num % 2 == 0]` creates a new list by iterating over each `num` in the `arr` list and only including the numbers that satisfy the condition `num % 2 == 0` (i.e., the number is even).

The function then returns the new list containing only the even numbers from the input list.

To test the function, you can use the `assert` statement provided in the original code. By calling `Split([1, 2, 3, 4, 5])`, the function will return `[2, 4]`, which matches the expected result.

This function can be used to find even numbers from any list of numbers by passing the list as an argument to the `Split` function.

Note: The original code also includes an assert statement to test the function's output. The `assert` statement is a debugging tool in Python that allows you to check if a condition is true. In this case, it is used to verify that the function returns the expected result for the given input list `[1, 2, 3, 4, 5]`. If the condition is not true, the program will raise an `AssertionError` exception.

Overall, this Python function provides a concise and efficient solution to find even numbers from a given list of numbers using a list comprehension.

```python
def Split(arr):
    return [num for num in arr if num % 2 == 0]

# Testing the function
assert Split([1, 2, 3, 4, 5]) == [2, 4