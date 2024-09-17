You can use the built-in function `set` to check if there is any value in the first sequence that exists in the second sequence. If there is, it means the two sequences have at least one common value.

Here is the Python function:

```
def overlapping(seq1, seq2):
    return set(seq1) & set(seq2)
```

This function will return a set containing the common values between the two sequences. If the sequences have no common values, it will return an empty set. The `assert` statement in the problem description is checking if the function returns an empty set for two sequences with no common values.

However, the problem description seems to be asking for a function that returns `True` if there is any common value and `False` otherwise. In this case, you can use the following function:

```
def overlapping(seq1, seq2):
    return bool(set(seq1) & set(seq2))
```

This function will return `True` if there are any common values and `False` otherwise. The `bool` function converts the set to a boolean value, where an empty set is considered `False` and a non-empty set is considered `True`. 