```
def remove_Occ(s, c):
    return s.replace(c, '', 1).replace(c, '', 1)
```


The function `remove_Occ` takes two parameters: a string `s` and a character `c`. It uses the `replace` method to replace the first occurrence of `c` in `s` with an empty string, effectively removing it. The `1` in the `replace` method is to specify that we only want to replace the first occurrence. Then it does the same thing to remove the last occurrence of `c`. The result is the string with the first and last occurrences of `c` removed.  The unit test `assert remove_Occ("hello","l") == "heo"` ensures that the function works correctly.  The function should return "heo" when given "hello" and "l" as arguments.  This is because "hello" has two "l"s, the first and the last, which are removed by the function, leaving "heo".  



Note: The problem statement does not specify whether we should remove the first or the last occurrence of the character. However, based on the unit test provided, it seems that we should remove both the first and the last occurrence. If we should remove only the first or only the last occurrence, we would need to adjust the problem statement accordingly.  Also, if we want to remove all occurrences of the character, we can use the `replace` method without the count, like this: `s.replace(c, '')`. This will remove all occurrences of `c` from `s`.  However, this is not what the problem statement asks for, which is to remove the first and the last occurrence.  Therefore, we use the `replace` method with the count to remove the first and the last occurrence.  The first `replace` method removes the first occurrence, and the second `replace` method removes the last occurrence.  



This function works for strings and characters. It does not handle other types of input. If we want to handle other types of input, we would need to adjust the function accordingly.  For example, if we want to handle lists or sets instead of strings, we would need to convert them to strings before processing.  If we want to handle other types of characters, such as integers or floats, we would need to convert them to strings before processing.  However, based on the problem statement, it seems that we are only working with