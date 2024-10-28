```
def Find_Min(lst):
    return min(lst, key=len)
```
This function uses the built-in min function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. The key argument of the min function is a function that takes one argument and returns one value. In this case, we use the len function as the key to find the sublist with the smallest length. 

The unit test `assert Find_Min([[1],[1,2],[1,2,3]]) == [1]` ensures that the function works correctly. It checks that when the input is `[[1],[1,2],[1,2,3]]`, the output is `[1]`, which is the sublist with the smallest length. 