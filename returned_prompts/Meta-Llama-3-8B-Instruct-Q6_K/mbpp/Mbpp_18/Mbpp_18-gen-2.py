```
def remove_dirty_chars(s, dirty_chars):
    return ''.join([c for c in s if c not in dirty_chars])
```


The problem asks to create a function that takes two strings as input and returns a new string where all the characters from the first string that are present in the second string are removed. 

For example, if the input strings are "probasscurve" and "pros", the function should return "bacuve" as the characters "p", "r", and "o" are present in "pros" and are removed from "probasscurve".

Here is a Python solution for this problem:

```
def remove_dirty_chars(s, dirty_chars):
    return ''.join([c for c in s if c not in dirty_chars])
```

This function uses a list comprehension to iterate over each character in the string `s`. If the character is not present in the string `dirty_chars`, it is added to the resulting list. Finally, the `join` method is used to convert the list of characters back into a string, which is then returned as the result. 

This solution passes the given unit test:

```
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
```


This unit test checks that the function correctly removes the characters "p", "r", and "o" from the string "probasscurve" when the string "pros" is used as the second input. The expected output is "bacuve", which is the same as the result returned by the function. 

Therefore, this solution correctly solves the problem and passes the given unit test. 