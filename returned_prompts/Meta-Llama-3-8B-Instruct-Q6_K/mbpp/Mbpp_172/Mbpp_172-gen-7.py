```
def count_occurance(s):
    return s.count('std')
```
The function `count_occurance` takes a string `s` as an argument and returns the number of times the string 'std' appears in `s`. The `count` method of a string in Python returns the number of non-overlapping occurrences of a substring in the string. In this case, we are using it to count the number of occurrences of the substring 'std'. 

The unit test `assert count_occurance("letstdlenstdporstd") == 3` ensures that the function works correctly. It checks if the function returns 3 when the input string is "letstdlenstdporstd", which is the expected output. 

For example, if we call `count_occurance("letstdlenstdporstd")`, the function will return `3` because the string 'std' appears three times in the given string. 