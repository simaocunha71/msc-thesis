```
def count_occurance(s):
    return s.count('std')
```


Explanation:
The task is to write a function that counts the number of occurrences of the string 'std' in a given string. 

The provided unit test suggests that the function should return 3 for the input "letstdlenstdporstd". 

The built-in method `count` in Python strings can be used to solve this problem. It returns the number of occurrences of the specified value in the string. In this case, the specified value is 'std'.

Here's the Python function that solves the problem:

```
def count_occurance(s):
    return s.count('std')
```

This function takes a string `s` as input and returns the number of occurrences of 'std' in `s`. The `count` method is used to achieve this. The function can be tested with the provided unit test:

```
assert count_occurance("letstdlenstdporstd") == 3
```


This test checks if the function returns 3 for the input "letstdlenstdporstd", which is the expected output. If the function is implemented correctly, the test should pass. 