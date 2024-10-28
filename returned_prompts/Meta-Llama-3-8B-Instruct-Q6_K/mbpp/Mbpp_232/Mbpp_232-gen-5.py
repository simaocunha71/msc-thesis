```
def largest_n_items(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:n]
```
The problem is asking you to create a function that takes a list of numbers and an integer n, and returns a list containing the n largest numbers from the input list.

The given unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` suggests that the function should return the n largest numbers from the list, in descending order.

Here's a Python solution that uses the built-in `sorted` function to sort the list in descending order, and then returns the first n items from the sorted list:
```
def largest_n_items(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:n]
```
This function works by first sorting the input list in descending order using the `sorted` function with the `reverse=True` argument. This gives us a list of numbers in descending order, with the largest number first. Then, we use list slicing to return the first n items from the sorted list, which are the n largest numbers from the original list. The `[:n]` part of the list slicing operation returns a new list containing the first n items from the original list. The `set` function can be used to remove duplicate values from the returned list, as shown in the unit test. However, in this case, we don't need to use `set` because the problem statement doesn't mention anything about removing duplicates. The function will return a list of the n largest numbers from the input list, in descending order, without any duplicates.