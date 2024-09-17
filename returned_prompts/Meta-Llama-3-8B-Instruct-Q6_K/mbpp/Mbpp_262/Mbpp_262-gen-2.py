```
def split_two_parts(lst, L):
    return lst[:L], lst[L:]
```



The problem is asking to create a function that takes a list and an integer L as input, and splits the list into two parts. The first part should have a length of L, and the function should return the resulting lists as a tuple.

The unit test `assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])` helps to clarify the problem by providing an example of how the function should behave.

The solution to this problem is to use Python's list slicing feature. The function can use `lst[:L]` to get the first L elements of the list, and `lst[L:]` to get the rest of the list. The resulting lists can then be returned as a tuple.

Here is the solution:
```
def split_two_parts(lst, L):
    return lst[:L], lst[L:]
```
This function works by taking the input list `lst` and integer `L`, and then returning a tuple containing two lists: `lst[:L]` which is the first `L` elements of the list, and `lst[L:]` which is the rest of the list. The `[:L]` and `[L:]` syntax is used to slice the list, effectively splitting it into two parts. The resulting lists are then returned as a tuple.