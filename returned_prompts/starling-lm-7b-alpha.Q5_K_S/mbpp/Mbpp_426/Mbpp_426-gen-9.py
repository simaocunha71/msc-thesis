```
def filter_oddnumbers(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result

```

Explanation:
The function `filter_oddnumbers` takes in a list of numbers as an argument. It initializes an empty list called `result` to store the odd numbers. Then, it iterates through each number in the input list using a for loop. Inside the loop, it checks if the number is odd by using the modulo operator (`number % 2 != 0`). If the condition is true, it appends the number to the `result` list. Finally, it returns the `result` list containing all the odd numbers.

In the given example, when `filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` is called, it will return `[1, 3, 5, 7, 9]` as the output, which are all the odd numbers from the input list.

You can test the function by running the assert statement provided in the question, which checks if the output of `filter_oddnumbers` with the given input list matches the expected result `[1, 3, 5, 7, 9]`. If the assertion passes, it means the function is correctly filtering odd numbers.

Note: The function `filter_oddnumbers` can be used with any list of numbers, not just the one provided in the example. You can pass different input lists to test the function and verify its correctness.

Here's an example of how you can use the `filter_oddnumbers` function:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_oddnumbers(numbers)
print(result)  # Output: [1, 3, 5, 7, 9]
```

In this example, the `numbers` list contains even and odd numbers. The `filter_oddnumbers` function is called with `numbers` as