```
def filter_oddnumbers(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
```

Explanation:
The function `filter_oddnumbers` takes a list of numbers as an argument. It initializes an empty list called `result` to store the odd numbers. Then, it iterates through each number in the input list using a `for` loop. Inside the loop, it checks if the current number is odd by using the modulo operator `%` to check if the number is not divisible by 2. If the number is odd, it is added to the `result` list using the `append` method. Finally, the function returns the `result` list containing all the odd numbers.

In the provided example, the function is called with the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. The expected output is `[1, 3, 5, 7, 9]`, which are all the odd numbers in the input list.

To verify the correctness of the function, you can use the `assert` statement to check if the function's output matches the expected result. If the function's output is not `[1, 3, 5, 7, 9]`, the `assert` statement will raise an error, indicating that the function is not correctly filtering odd numbers.

Overall, this function provides a straightforward solution to filter odd numbers from a given list of numbers.

```python
def filter_oddnumbers(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result
```

This function uses a `for` loop to iterate through each number in the input list `nums`. It checks if the current number is odd by using the modulo operator `%` to check if the number is not divisible by 2. If the number is odd, it is added to the `result` list using the