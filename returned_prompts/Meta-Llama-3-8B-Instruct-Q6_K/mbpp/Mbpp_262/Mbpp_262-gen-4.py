```
def split_two_parts(lst, L):
    return lst[:L], lst[L:]
```
The problem is asking to create a function that takes a list and an integer L as input, and then splits the list into two parts. The length of the first part should be L, and the function should return these two parts as a tuple.

The unit test provided suggests that the function should behave as follows: if the input list is [1,1,2,3,4,4,5,1] and L is 3, the function should return ([1, 1, 2], [3, 4, 4, 5, 1]).

To solve this problem, we can use Python's list slicing feature. We can use lst[:L] to get the first L elements of the list, and lst[L:] to get the rest of the list. We then return these two parts as a tuple.

Here's the solution:
```
def split_two_parts(lst, L):
    return lst[:L], lst[L:]
```
This function works by slicing the input list into two parts: the first L elements, and the rest of the list. The rest of the list is obtained by starting from the Lth element of the original list (which is at index L) and going to the end of the list. The two parts are then returned as a tuple.