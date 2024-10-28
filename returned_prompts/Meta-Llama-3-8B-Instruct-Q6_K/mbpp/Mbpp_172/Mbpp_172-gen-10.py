```
def count_occurance(s):
    return s.count('std')
```
This function uses the built-in string method `count()` which returns the number of occurrences of the substring 'std' in the given string `s`. 

The unit test `assert count_occurance("letstdlenstdporstd") == 3` ensures that the function works correctly by checking if the count of 'std' in the given string is 3, which is indeed the case. 

This solution is straightforward and efficient, with a time complexity of O(n), where n is the length of the input string.  It does not require any advanced techniques or data structures, making it easy to understand and implement.  



