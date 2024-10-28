```
def number_of_substrings(s):
    return sum(len(s)-i for i in range(len(s)+1))
```


The function `number_of_substrings(s)` counts the number of non-empty substrings of a given string `s`. It does this by summing the length of the string minus each index `i` from 0 to the length of the string. This is because each index `i` corresponds to a non-empty substring ending at index `i`.

For example, for the string "abc", the function returns 6 because there are 6 non-empty substrings: "a", "ab", "abc", "b", "bc", and "c".

The unit test `assert number_of_substrings("abc") == 6` verifies that the function is working correctly.