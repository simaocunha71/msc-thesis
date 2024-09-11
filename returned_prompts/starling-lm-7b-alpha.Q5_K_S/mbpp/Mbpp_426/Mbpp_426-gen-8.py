```
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 == 1]
```

Explanation:
The function `filter_oddnumbers` takes a list `lst` as input and returns a new list containing only the odd numbers from the original list. It does this by using a list comprehension to iterate over each element in the list and check if the number is odd (i.e., if the number modulo 2 is equal to 1). If the condition is true, the number is included in the new list.

To test the function, you can use the `assert` statement to check if the function returns the expected result when given the input `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. In this case, the expected output is `[1, 3, 5, 7, 9]`, which is the list of odd numbers from the original input list.

By using this function, you can easily filter out the odd numbers from any given list of numbers.

Here's an example usage of the function:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_oddnumbers(numbers)
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
```

This will output the list of odd numbers from the `numbers` list using the `filter_oddnumbers` function.

Overall, this solution provides a concise and efficient way to filter odd numbers from a given list of numbers.










































































```

```