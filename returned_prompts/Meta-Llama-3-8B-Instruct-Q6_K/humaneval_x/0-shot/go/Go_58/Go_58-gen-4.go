Here is the Python solution for the problem:

```Python
def Common(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    common = set1 & set2
    return sorted(list(common))
```
This function first converts the input lists to sets, which are unordered collections of unique elements. Then it calculates the intersection of the two sets, which is the set of elements that are common to both sets. Finally, it converts the result back to a list and sorts it. The `sorted` function is used to sort the list in ascending order.

Here is the Python code with examples:

```Python
print(Common([1, 4, 3, 34, 653, 2, 5], [5, 7,