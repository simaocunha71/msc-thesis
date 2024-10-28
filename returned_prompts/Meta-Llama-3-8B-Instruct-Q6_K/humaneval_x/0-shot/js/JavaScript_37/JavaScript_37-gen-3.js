Here is a Python solution for the problem:
```
def sort_even_indices(lst):
    return [x if i % 2 == 0 else y for i, (x, y) in enumerate(sorted((x, y) for x, y in zip(lst, lst[1:])))]
```
Here is a breakdown of the solution:
- `zip(lst, lst[1:])` creates pairs of consecutive elements in the list.
- `sorted((x, y) for x, y in zip(lst, lst[1:]))` sorts these pairs based on the second element in each pair.
- `enumerate` is used to keep track of the indices while iterating over the sorted pairs.
- The list comprehension then creates a new list where the elements at even indices are the sorted elements from the previous step, and the elements at odd indices are the same as in the original list.