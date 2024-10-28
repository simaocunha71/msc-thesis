You can use list comprehension to achieve this. Here's the solution:
```
def merge(lists):
    return [list(map(lambda x: x[0], lists)), list(map(lambda x: x[1], lists))]
```
This function uses the `map` function to apply a lambda function to each sublist in the input list. The lambda function extracts the first element (`x[0]`) or the second element (`x[1]`) from each sublist. The results are then converted to lists using the `list` function.

For example, if you call the function with the input `[['x', 'y'], ['a', 'b'], ['m', 'n']]`, it will return `[['x', 'a', 'm'], ['y', 'b', 'n']]`.

The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` ensures that the function works correctly. It checks that the output of the function is equal to the expected result. If the output is not equal to the expected result, the test will fail. This helps to ensure that the function is working correctly.