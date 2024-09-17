```
def Extract(lists):
    return [i[0] for i in lists]
```
The function `Extract` takes a list of lists as input. It uses a list comprehension to iterate over each sublist and return the first element of each sublist. The result is a list of the first elements of the sublists.

The unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` demonstrates the functionality of the function. It checks that the function returns the correct output for a given input. In this case, the input is a list of lists `[[1, 2], [3, 4, 5], [6, 7, 8, 9]]`, and the expected output is `[1, 3, 6]`. The function `Extract` returns the expected output, so the unit test passes.