Here is the Python function for the problem:

```python
def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))
```

In this function, `^` operator is used to find the dissimilar elements in two sets. This operator returns a set that contains all items from both sets, but not the items present in both sets.

Now, let's test the function with the given input:

```python
print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))  # Outputs: (3, 6, 7, 10)
```
This output is expected because 3 and 6 are in the first tuple but not in the second and 7 and 10 are in the second tuple but not in the first.
"""

# ╔═╡ 0b1f6a54-81c9-4b9e-87b1-3e51b1a0ad40
md"""
