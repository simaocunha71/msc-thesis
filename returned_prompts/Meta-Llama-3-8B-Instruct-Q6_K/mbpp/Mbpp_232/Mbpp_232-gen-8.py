```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```







The problem is asking to create a function that takes a list and an integer n as inputs, and returns a list containing the n largest items from the original list. The function should return the n largest unique items if there are duplicate values in the list.

Here's the solution in Python:

```
def larg_nnum(lst, n):
    return sorted(set(lst), reverse=True)[:n]
```

Explanation:
1. `set(lst)` is used to remove duplicates from the list.
2. `sorted(..., reverse=True)` is used to sort the list in descending order.
3. `[:n]` is used to select the first n items from the sorted list.

For example, if the input list is `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` and `n` is `2`, the output will be `[100, 90]`, which are the two largest unique items in the list. The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` confirms this.