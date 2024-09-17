```
def remove_dirty_chars(s1, s2):
    return ''.join([c for c in s1 if c not in s2])
```


This function uses list comprehension to create a new list that includes only the characters from `s1` that are not in `s2`. The `join` method is then used to concatenate these characters into a single string. The unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'` ensures that the function works correctly. For example, in this test, the function should remove the characters 'p', 'r', 'o' and 's' from the first string, leaving the remaining characters 'bacuve'. 