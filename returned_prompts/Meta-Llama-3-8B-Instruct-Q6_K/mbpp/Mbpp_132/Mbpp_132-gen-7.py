```
def tup_string(tup):
    return ''.join(tup).replace(' ', '')
```



Explanation:
The task is to create a function that takes a tuple as an input and returns a string. The string should be a combination of all the elements in the tuple without any spaces.

The unit test provided helps in understanding the expected output. The test case `assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")` clarifies that the function should concatenate all the elements in the tuple and remove any spaces.

The solution uses the `join` function to concatenate all the elements in the tuple into a string, and then the `replace` function to remove any spaces. This results in a string that is a combination of all the elements in the tuple without any spaces. 