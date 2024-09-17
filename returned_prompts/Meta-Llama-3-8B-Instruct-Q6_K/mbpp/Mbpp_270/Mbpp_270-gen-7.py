```
def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)
```
This function uses the `enumerate` function to iterate over the list and get the index `i` of each element. It then uses a generator expression to filter out the elements at odd positions (`i % 2 != 0`) and the elements that are not even (`num % 2 != 0`). The `sum` function is then used to calculate the sum of the filtered elements. 

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` checks that the function returns the correct sum for the given list. 

This function assumes that the input list is not empty and that the elements in the list are integers. If the input list can be empty or contain non-integer elements, additional error handling may be needed. 

For example, to handle the case where the input list is empty, you could add a check at the beginning of the function:
```
def sum_even_and_even_index(lst):
    if not lst:
        return 0
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)
```
This would return 0 if the input list is empty, rather than raising an exception.  Similarly, you could add a check to handle the case where an element in the list is not an integer:
```
def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and isinstance(num, int) and num % 2 == 0)
```
This would skip over any elements in the list that are not integers, rather than raising an exception.  Depending on the specific requirements of your function, you may need to add additional error handling or checks.  For example, you might want to raise an exception if the input list contains non-integer elements, or if the input list is empty.  The exact error handling you use will depend on the specific requirements of your function.  In general, it's a good idea to include clear and informative error messages, and to handle errors in a way that is consistent with the rest of your code.  For example:
```
def sum_even_and_even_index(lst):
    if