```
def overlapping(seq1, seq2):
    for element in seq1:
        if element in seq2:
            return True
    return False
```
This function takes two sequences as input and checks if any element in the first sequence exists in the second sequence. It returns True if any element is found, and False if not. The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function correctly returns False for non-overlapping sequences. 

In this function, we iterate over each element in the first sequence. If we find an element that exists in the second sequence, we immediately return True. If we finish iterating over the first sequence without finding any overlapping elements, we return False. 

This function assumes that the sequences are iterable (such as lists, tuples, or strings), and that the elements are hashable (such as integers, floats, or strings). It does not work correctly with unhashable elements (such as lists or dictionaries), because these cannot be used as dictionary keys. 

The time complexity of this function is O(n*m), where n is the length of the first sequence and m is the length of the second sequence, because in the worst case we may need to check every element in the first sequence against every element in the second sequence. The space complexity is O(1), because we only use a constant amount of space to store the result and any temporary variables. 