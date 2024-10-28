```
def Find_Max_Length(lists):
    return max(len(sublist) for sublist in lists)
```
This function uses a generator expression to iterate over the sublists in the input list, calculates the length of each sublist using the len() function, and then uses the built-in max() function to find the maximum length.

The unit test `assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4` helps to clarify that the function should find the length of the longest sublist. In this case, the longest sublist is [5,6,7,8] with a length of 4. 

So, the output of the function `Find_Max_Length([[1],[1,4],[5,6,7,8]])` should be 4.  This is what the unit test is asserting.  The function will return 4, which matches the expected output.  Therefore, the function passes the unit test. 