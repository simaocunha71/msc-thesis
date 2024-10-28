```
def overlapping(seq1, seq2):
    for element in seq1:
        if element in seq2:
            return True
    return False
```


Explanation:
The function `overlapping` takes two sequences as input and checks if any element from the first sequence exists in the second sequence. It iterates over each element in the first sequence and checks if it is present in the second sequence using the `in` operator. If it finds any matching element, it returns `True`. If it doesn't find any matching element after iterating over all elements in the first sequence, it returns `False`.

The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function returns `False` when there are no overlapping elements between the two sequences. This is because the elements in the first sequence are distinct and do not appear in the second sequence. Therefore, the function correctly identifies that there are no overlapping elements and returns `False`.