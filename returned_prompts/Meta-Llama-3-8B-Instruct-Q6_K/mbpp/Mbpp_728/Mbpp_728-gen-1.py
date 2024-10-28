```
def sum_list(a, b):
    return [x+y for x,y in zip(a,b)]
```


Explanation: 
We can use list comprehension and the built-in `zip` function to achieve this. The `zip` function pairs up the elements of the two lists, and the list comprehension adds these pairs together. The result is a new list where each element is the sum of the corresponding elements in the input lists. The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` shows that this function works correctly. 

This function assumes that both input lists have the same length. If the lists are of different lengths, the `zip` function will stop at the end of the shorter list, effectively ignoring the remaining elements in the longer list. If you want to handle lists of different lengths differently, you would need to add additional logic to the function. 

For example, you could pad the shorter list with a default value (such as 0), or you could raise an error if the lists are of different lengths. 

Here is an example of how you could pad the shorter list with a default value:
```
def sum_list(a, b):
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    return [x+y for x,y in zip(a,b)]
```  This version of the function will add zeros to the end of the shorter list to make it the same length as the longer list, and then proceed to add the corresponding elements of the two lists together.  This way, the function will work correctly even if the input lists are of different lengths.  However, this version of the function will still raise an error if the lists are of very different lengths, because it will add a large number of zeros to the end of one of the lists.  If you want to handle lists of very different lengths in a more robust way, you will need to add additional logic to the function.  For example, you could decide to ignore the extra elements in the longer list, or you could decide to raise an error if the lists are of very different lengths.  It depends on the specific requirements of your problem.  In this case, the problem statement does not specify what to do if the lists are of very different lengths, so the function will raise an error if the lists are