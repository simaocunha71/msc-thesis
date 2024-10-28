```
def recursive_list_sum(lst):
    total_sum = sum(i for i in lst if isinstance(i, int))
    for i in lst:
        if isinstance(i, list):
            total_sum += recursive_list_sum(i)
    return total_sum
```
The problem is asking to create a function that takes a list as input, flattens it (by recursively going through the list and adding all its elements), and then sums all the elements in the flattened list.

The unit test provided, `assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21`, shows that the function should return the sum of all elements in the list, including nested lists. For example, the list `([1, 2, [3,4],[5,6]])` should return `21` because `1+2+3+4+5+6=21`.

The solution uses a recursive approach. It goes through each element in the list. If the element is an integer, it adds it to the total sum. If the element is a list, it recursively calls itself on that list and adds the result to the total sum. This way, it flattens the list and sums all its elements. The base case for the recursion is when the element is not a list, in which case it is either an integer (which is added to the sum) or something else (which is ignored). The function returns the total sum at the end.  ```python
def recursive_list_sum(lst):
    total_sum = sum(i for i in lst if isinstance(i, int))
    for i in lst:
        if isinstance(i, list):
            total_sum += recursive_list_sum(i)
    return total_sum
```
This function should pass the provided unit test.  ```python
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
```  ```python
assert recursive_list_sum([1, 2, 3, 4, 5, 6]) == 21
```  ```python
assert recursive_list_sum([1, 2, [3,4],[5,6],[7,8,9]]) == 36
```  ```python
assert recursive_list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
```  ```python
assert recursive_list_sum([1, 2,