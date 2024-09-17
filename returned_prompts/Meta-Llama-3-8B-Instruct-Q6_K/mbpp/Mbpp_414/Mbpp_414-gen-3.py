```
def overlapping(seq1, seq2):
    for i in seq1:
        for j in seq2:
            if i == j:
                return True
    return False
```
The function `overlapping` checks if any value in `seq1` exists in `seq2` or vice versa. It iterates over each value in `seq1` and checks if it exists in `seq2`. If a match is found, it returns `True`. If no match is found after checking all values in `seq1`, it returns `False`. 

The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function correctly returns `False` when no value in `seq1` exists in `seq2`. 

This function assumes that the sequences are lists or other iterable types. It also assumes that the values in the sequences are hashable (i.e., they can be used as dictionary keys). If the sequences contain unhashable values (such as lists or dictionaries), a different approach would be needed. 

Note that this function has a time complexity of O(n*m) where n and m are the lengths of the input sequences, because it uses nested loops to check for matches. This may not be efficient for very large sequences. A more efficient approach might be to use a set to keep track of the values in `seq1` and then check if each value in `seq2` is in the set. This would have a time complexity of O(n+m). 

Here is an example of how you could implement this more efficient approach:

```
def overlapping(seq1, seq2):
    set1 = set(seq1)
    for i in seq2:
        if i in set1:
            return True
    return False
```  ```python
def overlapping(seq1, seq2):
    set1 = set(seq1)
    for i in seq2:
        if i in set1:
            return True
    return False
```  ```python
def overlapping(seq1, seq2):
    set1 = set(seq1)
    for i in seq2:
        if i in set1:
            return True
    return False
```  ```python
def overlapping(seq1, seq2):
    set1 = set(seq1)
    for i in seq2:
        if i in set1:
            return True
    return False
```  ```python
def