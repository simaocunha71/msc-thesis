You can solve this problem by defining a regular expression pattern that matches a string that starts with 'a' and ends with 'b'. The pattern will be 'a.*b', where '.*' is a wildcard that matches any characters.

Here is the solution in Python:
```
import re

def match_string(s):
    pattern = re.compile('a.*b')
    return bool(pattern.match(s))
```
This function uses the `re` module to compile the pattern 'a.*b' and then uses the `match` method to check if the pattern matches the input string `s`. The `bool` function is used to convert the match object to a boolean value, which is `True` if the pattern matches and `False` otherwise.

You can test this function with the following code:
```
assert match_string("aabbbb")
```
This should return `True` because the string "aabbbb" matches the pattern 'a.*b'. If you test the function with a string that does not match the pattern, such as "abc", it should return `False`. For example:
```
assert not match_string("abc")
```
This should also return `True` because the string "abc" does not match the pattern 'a.*b'.