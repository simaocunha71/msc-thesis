```
def overlapping(seq1, seq2):
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                return True
    return False
```
This function takes two sequences as input and checks if any value in the first sequence exists in the second sequence. It returns `True` if any value is found and `False` otherwise.

The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function returns `False` when no values from `seq1` exist in `seq2`. 

However, this function has a time complexity of O(n*m) where n and m are the lengths of the two sequences, which is not efficient for large sequences. A more efficient solution would be to convert the second sequence to a set and then check for membership in the set. This would reduce the time complexity to O(n) for the set conversion and O(1) for the membership check. Here is the optimized function:

```
def overlapping(seq1, seq2):
    set2 = set(seq2)
    for val in seq1:
        if val in set2:
            return True
    return False
```  ```python
def overlapping(seq1, seq2):
    set2 = set(seq2)
    for val in seq1:
        if val in set2:
            return True
    return False
```
This function converts the second sequence to a set and then checks for membership in the set. If any value from `seq1` is found in the set, it returns `True`. If no values are found, it returns `False`. This function has a time complexity of O(n+m) where n and m are the lengths of the two sequences, which is more efficient than the previous solution.  ```python
def overlapping(seq1, seq2):
    set2 = set(seq2)
    for val in seq1:
        if val in set2:
            return True
    return False
```
This function converts the second sequence to a set and then checks for membership in the set. If any value from `seq1` is found in the set, it returns `True`. If no values are found, it returns `False`. This function has a time complexity of O(n+m) where n and m are the lengths of the two sequences, which is more efficient than the previous solution