
Here's one possible solution to the problem:

```python
def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2 != 0]

    sorted_even = sorted([l[i] for i in even_indices])

    return [l[i] if i in odd_indices else sorted_even[i//2] for i in range(len(l))]
```

This function first creates two separate lists of even and odd indices. It then sorts the values at the even indices of the original list and assigns them to `sorted_even`. Finally, it constructs a new list where the original values at odd indices are kept and the original values at even indices are replaced by the sorted values from `sorted_even`.

Here's the function in action:

```python
print(sort_even([5, 6, 3, 4]))  # prints: [3, 6, 5, 4]
print(sort_even([1, 2, 3]))  # prints: [1, 2, 3]
```

The function correctly sorts the values at the even indices while keeping the original values at the odd indices intact.

Note: The function assumes that the input list `l` is not empty. It's a good idea to add a check at the beginning of the function to ensure this.

```python
def sort_even(l: list):
    if not l:
        return []
    # ...
```

This ensures that the function doesn't raise an error if it's given an empty list.

```python
print(sort_even([]))  # prints: []
```

In this case, the function correctly returns an empty list, as expected.

```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l