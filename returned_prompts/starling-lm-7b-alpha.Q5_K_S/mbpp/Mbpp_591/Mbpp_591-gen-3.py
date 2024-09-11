Here's a Python function that swaps the first and last elements in a list:

```python
def swap_List(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp
    return input_list
```

You can test the function with the given example:

```python
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

The `swap_List` function takes an input list as a parameter. It creates a temporary variable `temp` and assigns the first element of the list to it. Then, it assigns the last element of the list to the first element, and finally assigns the value of `temp` (the original first element) to the last element. The function returns the modified list.

When you run the assert statement, it checks if the function correctly swaps the first and last elements in the list. In this case, the assertion passes because the output of `swap_List([12, 35, 9, 56, 24])` is `[24, 35, 9, 56, 12]`, which is the expected result.

```python
def swap_List(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp
    return input_list

# Testing the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

The `assert` statement is used to check if a condition is true. In this case, it checks if the function `swap_List` correctly swaps the first and last elements in the input list. If the condition is not true, the program will raise an `AssertionError` with an error message.

The `swap_List` function can be used to interchange the first and last elements in any list,