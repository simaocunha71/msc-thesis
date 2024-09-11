```
def larg_nnum(list,num):
    list.sort(reverse=True)
    return list[:num]
```

Here's an example of how you can use the function:

```python
list = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
num = 2
print(larg_nnum(list,num))
```

The output will be `[100,90]`, which are the 2 largest items in the list.

The function works by first sorting the list in descending order using the `sort()` method with the `reverse=True` parameter. Then, it uses list slicing to return a new list containing the first `num` elements of the sorted list, which are the `num` largest items.

Note that the original list is modified in place by the `sort()` method, but the function returns a new list that contains the `num` largest items, leaving the original list unchanged.

The time complexity of this function is O(n log n) due to the sorting step, and the space complexity is O(n) due to the return value.

Here's a breakdown of the steps in the function:

1. Sort the list in descending order using the `sort()` method with `reverse=True`. This has a time complexity of O(n log n) and modifies the list in place.
2. Return a new list containing the first `num` elements of the sorted list using list slicing. This has a time complexity of O(n) and a space complexity of O(n).

Overall, the function has a time complexity of O(n log n) and a space complexity of O(n).

The provided assertion checks that the function correctly returns the set of the two largest numbers from the list `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` when `num` is set to 2. The `set()` function is used to convert the list to a set