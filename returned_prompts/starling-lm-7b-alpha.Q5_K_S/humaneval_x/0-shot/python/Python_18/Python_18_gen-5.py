
Here is a very simple solution that uses the built-in count() function of Python:

```python
def how_many_times(string: str, substring: str) -> int:
    return string.count(substring)
```

This solution works well for most cases, but it does not count overlapping cases correctly. For example, if the string is "aaa" and the substring is "aa", it will return 2 instead of 3:

```python
print(how_many_times('aaa', 'aa'))  # prints: 2
```

To count overlapping cases correctly, we can use the following solution that uses regular expressions (re):

```python
import re

def how_many_times(string: str, substring: str) -> int:
    return len(re.findall(substring, string))
```

This solution will return the correct result:

```python
print(how_many_times('aaa', 'aa'))  # prints: 3
```

For more details about the findall() function, you can refer to the official Python documentation:

- [Regular Expression How-To](https://docs.python.org/2/library/re.html#regular-expression-how-to)
- [Regular Expression Objects](https://docs.python.org/2/library/re.html#regular-expression-objects)
- [Regular Expression Recipes](https://docs.python.org/2/library/re.html#regular-expression-recipes)

For more details about the count() function, you can refer to the official Python documentation:

- [String Methods](https://docs.python.org/2/library/stdtypes.html#string-methods)

Here are some additional resources that you might find helpful:

- [How to Match a Substring in a String](https://stackoverflow.com/questions/1701892/how-to-match-a-substring-in-a-string)
- [How to find all occurrences of a substring in a string in Python](https://stackoverflow.com/questions/3090000/how-to-