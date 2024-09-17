```
def overlapping(seq1, seq2):
    for i in seq1:
        for j in seq2:
            if i == j:
                return True
    return False
```


This function checks if any value in the first sequence exists in the second sequence. It uses two nested for loops to iterate over the elements in both sequences and returns True as soon as it finds a match, and False if it doesn't find any match after checking all elements. This solution has a time complexity of O(n*m) where n and m are the lengths of the sequences. 

For example, if we call `overlapping([1,2,3,4,5],[6,7,8,9])`, the function will return False because there are no common elements in the two sequences. If we call `overlapping([1,2,3],[2,3,4])`, the function will return True because the element 2 and 3 are common in both sequences. 





This problem can also be solved using sets. Here's how you can do it:

```
def overlapping(seq1, seq2):
    return set(seq1) & set(seq2)
```

This function converts the sequences to sets, which are unordered collections of unique elements. The `&` operator returns a set containing all elements that are in both sets. If there are any common elements, the function will return a non-empty set. If there are no common elements, the function will return an empty set. This solution has a time complexity of O(n + m) where n and m are the lengths of the sequences. 





Here's how you can use this function in a unit test:

```
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
```


This unit test checks if the function correctly returns False when there are no common elements in the two sequences. You can add more unit tests to cover different scenarios. 





Note: The problem statement doesn't specify what the function should return if there are any common elements in the sequences. However, based on the provided unit test, it seems that the function should return a boolean value indicating whether there are any common elements or not. If you want the function to return the common elements themselves, you can modify the function accordingly. 





Also, the problem statement doesn't specify whether the sequences are lists or not. However, based on the provided unit test, it seems that the function should