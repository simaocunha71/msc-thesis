```
def count_integer(my_list):
    ct = 0
    for i in my_list:
        if isinstance(i, int):
            ct += 1
    return ct
```

Explanation:
The function `count_integer` takes a list `my_list` as a parameter. It initializes a counter variable `ct` to 0. Then it iterates through each element `i` in the list. For each element, it checks if the element is an instance of the `int` class using the `isinstance` function. If the element is an integer, it increments the counter variable by 1. Finally, it returns the total count of integer elements in the list.

To test the function, you can use the `assert` statement to verify if the function returns the expected result. In this case, `assert count_integer([1,2,'abc',1.2]) == 2` checks if the function correctly counts the number of integer elements in the given list `[1,2,'abc',1.2]` and returns the expected result of 2.

You can modify the `count_integer` function to handle other types of elements as per your requirement.

Overall, this function provides a reliable and efficient way to count the number of integer elements in a given list in Python.

Note: Make sure to use the correct indentation when defining the function and the `assert` statement.

Additionally, it's worth mentioning that the `isinstance(i, int)` condition in the function will only work if all integer values in the list are of type `int`. If the list contains integers of other types (e.g., `long`), you may need to modify the condition accordingly.

Here are some additional tips to improve the function:

1. To avoid the need for explicit type checking, you can use `isinstance(i, (int, long))` to check if the element is an integer or a long integer. However, keep in mind that the `long` type is not available in Python 3.x.

2. If you are using Python 3.x, you can simplify the function by using the `any` function along with a generator expression. Here's an example:

```python
def count_