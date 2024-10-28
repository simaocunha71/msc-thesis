```
def Find_Max_Length(lists):
    max_len = 0
    for lst in lists:
        max_len = max(max_len, len(lst))
    return max_len
```
The problem is asking to find the length of the longest sublist in a given list of lists. The function `Find_Max_Length` takes a list of lists as an argument and returns the length of the longest sublist.

The unit test `assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4` helps to clarify the problem by providing an example of the expected output.

The solution is a simple loop that iterates over the list of lists, keeping track of the maximum length found so far. The maximum length is updated at each iteration if a longer sublist is found. Finally, the function returns the maximum length found.

For example, if the input is `[[1],[1,4],[5,6,7,8]]`, the function will return `4` because the longest sublist is `[5,6,7,8]` which has a length of `4`. 