```
def add_string(lst, f_str):
    return [f_str.format(i) for i in lst]
```

Explanation:

The function add_string takes a list and a format string as inputs. It uses a list comprehension to iterate over each element in the list and apply the format string to it. The format string uses the placeholder {0} to indicate the position of the element in the list. The format method of the string class is then used to insert the element into the format string, resulting in a new list where each element has been formatted according to the input format string.

The assert statement is used to verify the correctness of the function. It asserts that when the function add_string is called with the input [1,2,3,4] and the format string 'temp{0}', the output should be ['temp1', 'temp2', 'temp3', 'temp4']. If the assertion is true, it means that the function is working correctly and correctly applies the format string to each element in the list.

Overall, this code provides a solution to the problem of applying a given format string to all elements in a list.

```python
def add_string(lst, f_str):
    return [f_str.format(i) for i in lst]
```

This function takes a list and a format string as inputs and returns a new list where each element has been formatted according to the input format string. It uses a list comprehension to iterate over each element in the input list and applies the format string using the format method of the string class. The result is a new list with the formatted elements.

The assert statement is used to verify the correctness of the function. It asserts that when the function add_string is called with the input [1,2,3,4] and the format string 'temp{0}', the output should be ['temp1', 'temp2', 'temp3', 'temp4']. If the assertion is true, it means that the function is working correctly and correctly applies the format string to each element in the list.

In summary, this code provides a solution to the problem of applying a given format string to all elements in a list, and it includes a test case to verify the correctness of the function.