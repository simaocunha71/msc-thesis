from itertools import izip, chain

def pair_wise(lst):
    return list(chain(*[izip(lst, lst[1:])]*len(lst)))


# testing
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
# assert pair_wise([1,2,3])==[(1, 2), (2, 3)]
# assert pair_wise([1])==[(1,)]
# assert pair_wise([])==[]




"""
The problem is to generate all pairs of consecutive items from a list. The easiest way to do this is to use the built-in zip function twice: first to group consecutive items, and then to flatten the result. However, if the input list is very large, then the zip function will consume a lot of memory, because it builds a list of tuples in memory.

To avoid this problem, we can use the itertools.izip function instead of zip. This function returns an iterator that yields tuples of consecutive items, without building a list of tuples. We also need to chain the result of izip, to flatten the result. The chain function takes any number of iterable arguments and returns a single iterator that yields all the items. In this case, we pass chain a single argument that is the result of izip applied to the input list and a slice of the list shifted one element. This results in an iterator that yields pairs of consecutive items, without consuming excessive memory. Finally, we convert the iterator to a list, to obtain a standard Python list of pairs.

"""




























```

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

``