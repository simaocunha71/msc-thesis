```
def remove_dirty_chars(s, dirty_chars):
    return ''.join([c for c in s if c not in dirty_chars])
```
This function uses a list comprehension to iterate over each character `c` in the string `s`. It checks if `c` is not present in the string `dirty_chars` using the `not in` operator. If `c` is not present in `dirty_chars`, it includes `c` in the list. Finally, it joins all the characters in the list using the `join` method to form the resulting string. 

This solution passes the given unit test:
```
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
```  This test case checks if the function correctly removes the characters 'p', 'r', 'o', 's' from the string "probasscurve" and returns the resulting string 'bacuve'. 