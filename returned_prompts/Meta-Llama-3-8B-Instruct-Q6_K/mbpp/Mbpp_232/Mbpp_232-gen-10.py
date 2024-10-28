```
def largest_nnums(lst, n):
    return sorted(lst, reverse=True)[:n]
```





The problem is asking to create a function that takes a list and an integer n as input, and returns a list containing the n largest items from the list.

The unit test provided, `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])`, suggests that the function should return the n largest unique items from the list.

Here is the solution:
```
def largest_nnums(lst, n):
    return sorted(set(lst), reverse=True)[:n]
```
This function first converts the list to a set to remove duplicates, then sorts the set in descending order, and finally returns the n largest items. The `[:n]` slice is used to get the first n items from the sorted list.

The `sorted` function is used to sort the set in descending order, and the `set` function is used to remove duplicates. The `reverse=True` argument is used to sort the set in descending order. The `[:n]` slice is used to get the first n items from the sorted list.