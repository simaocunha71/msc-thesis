```
def overlapping(seq1, seq2):
    return any(i in seq2 for i in seq1)
```
This function uses the built-in any() function and a generator expression to check if any element in seq1 exists in seq2. If any element is found in seq2, the function returns True. If not, it returns False. The unit test `assert overlapping([1,2,3,4,5],[6,7,8,9]) == False` ensures that the function correctly returns False when there are no overlapping elements. 

Here is the breakdown of the function:
- `any(i in seq2 for i in seq1)`: This is a generator expression that checks if each element `i` in `seq1` exists in `seq2`. If any element is found in `seq2`, the function returns `True`.
- `return any(...)`: This line returns the result of the generator expression. If any element is found in `seq2`, the function returns `True`. If not, it returns `False`. 