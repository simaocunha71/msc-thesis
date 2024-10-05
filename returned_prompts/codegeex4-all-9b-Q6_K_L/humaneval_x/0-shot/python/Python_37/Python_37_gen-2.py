```python


def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [l[i] for i in range(0, len(l), 2)]
    even_indices.sort()
    l_sorted = [even_indices.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
    return l_sorted

```
