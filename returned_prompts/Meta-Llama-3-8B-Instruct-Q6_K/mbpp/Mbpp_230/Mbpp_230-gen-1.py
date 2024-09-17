```
def replace_blank(s, c):
    return s.replace(' ', c)
```
This function uses the built-in string method `replace()` to replace all blank spaces in the string `s` with the character `c`. The `replace()` method returns a copy of the string where all occurrences of a substring have been replaced with another substring.

For example, if you call `replace_blank("hello people", "@")`, it will return `"hello@people"`. The blank space in the string has been replaced with the `@` character. This is confirmed by the unit test `assert replace_blank("hello people",'@')==("hello@people")`.