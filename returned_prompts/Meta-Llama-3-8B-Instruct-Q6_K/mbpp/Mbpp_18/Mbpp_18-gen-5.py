```
def remove_dirty_chars(s1, s2):
    return "".join([c for c in s1 if c not in s2])
```


The function `remove_dirty_chars` takes two strings, `s1` and `s2`, as input. It returns a new string that is the result of removing all characters from `s1` that are present in `s2`.

The function uses a list comprehension to iterate over each character `c` in `s1`. For each character, it checks if `c` is not in `s2` using the `in` operator. If `c` is not in `s2`, it includes `c` in the resulting list. Finally, it uses the `join` method to concatenate all the characters in the list into a single string.

For example, if `s1` is "probasscurve" and `s2` is "pros", the function would return the string "bacuve", which is the result of removing all characters from "probasscurve" that are present in "pros". This is confirmed by the unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'`.