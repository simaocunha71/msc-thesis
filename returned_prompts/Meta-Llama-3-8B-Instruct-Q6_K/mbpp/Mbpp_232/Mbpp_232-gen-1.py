You can solve this problem by using the built-in `sorted` function in Python to sort the list in descending order, then return a list containing the first `n` items from the sorted list.

Here's the solution:
```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```
This function sorts the input list `lst` in descending order using the `sorted` function with the `reverse=True` argument. It then returns a list containing the first `n` items from the sorted list using slicing (`[:n]`).

The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` ensures that the function returns the correct result. It checks that the function returns a list containing the two largest items from the input list, which are 100 and 90.

Note that the `set` function is used to convert the list to a set, which removes duplicates, to ensure that the test checks for the correct order of the largest items. If the input list contains duplicate items, the function will return the correct order of the largest items, but the set will contain fewer items than the original list. In this case, the test will pass if the function returns the correct order of the largest items, even if the set contains fewer items than the original list.