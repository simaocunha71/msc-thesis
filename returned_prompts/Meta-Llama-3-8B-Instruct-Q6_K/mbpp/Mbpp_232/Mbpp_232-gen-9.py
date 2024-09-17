```
def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]
```
This problem is asking you to create a function that takes a list and an integer as input, and returns a new list containing the n largest items from the original list.

The given unit test suggests that the function should return a list of the n largest numbers in the list, and that ties should be broken by returning the first occurrence of the tied value.

Here's how you can solve this problem in Python:
```
def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]
```
This function sorts the input list in descending order (i.e., largest to smallest), and then returns a new list containing the first n items from the sorted list. This ensures that the n largest items from the original list are returned.

For example, if you call `larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2)`, the function will return `[100, 90]`, which are the two largest numbers in the input list. The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` passes because the function returns the correct n largest numbers.