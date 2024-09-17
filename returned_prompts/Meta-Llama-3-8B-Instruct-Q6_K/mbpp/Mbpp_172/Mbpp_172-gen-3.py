```
def count_occurance(s):
    return s.count('std')
```


This function counts the number of occurrences of the string 'std' in the given string `s`. It uses the built-in `count` method of Python strings, which returns the number of non-overlapping occurrences of the specified substring in the given string. The function takes a string as input and returns an integer representing the count of occurrences.

The unit test `assert count_occurance("letstdlenstdporstd") == 3` ensures that the function correctly counts the occurrences of 'std' in the given string. If the function is implemented correctly, this test will pass, indicating that the function works as expected.