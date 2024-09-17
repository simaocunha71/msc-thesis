```
def remove_dirty_chars(s1, s2):
    return "".join([c for c in s1 if c not in s2])
```
The unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'` suggests that we need to remove all characters from the first string that are present in the second string. 

We can achieve this using a list comprehension and the `join` function in Python. The list comprehension iterates over each character in the first string and checks if it is not present in the second string. If it's not present, it adds the character to the list. Finally, it joins all characters in the list into a single string and returns it. 

In the given example, the function removes all characters 'p', 'r', 'o', and 's' from the first string "probasscurve" because these characters are present in the second string "pros". The result is 'bacuve'. 