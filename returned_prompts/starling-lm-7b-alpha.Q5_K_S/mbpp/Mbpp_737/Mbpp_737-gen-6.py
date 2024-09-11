Here is one possible solution:

```python
import re

def check_str(s):
    pattern = "^[aeiou]"
    if re.match(pattern, s):
        print("True")
    else:
        print("False")
```

Explanation:
This function first creates a regex pattern that matches any of the five vowels (a, e, i, o, u). It then uses the `re.match()` function to check whether the start of the input string matches the pattern. If it does, the function prints True; otherwise, it prints False.

```python
check_str("annie")
```

In this example, "annie" starts with the vowel 'a', so the function will print True.

```python
check_str("bob")
```

In this example, "bob" does not start with a vowel, so the function will print False.

```python
check_str("Alice")
```

In this example, "Alice" starts with the vowel 'A', so the function will print True.

Note that in the regex pattern, the caret (`^`) denotes the start of the string, and the dollar sign (`$`) denotes the end of the string. The square brackets (`[]`) contain the set of characters to match, and the `*` denotes zero or more of the preceding character.

Overall, this solution is an effective and concise way to determine whether a given string starts with a vowel using regex in Python.

```python
def check_str(s):
    pattern = "^[aeiou]"
    if re.match(pattern, s):
        print("True")
    else:
        print("False")
```

This function can be used to check whether a string starts with a vowel by passing the string as an argument to the `check_str()` function. The function will then print True if the string starts with a vowel, and False otherwise.

```python
check_str("annie")
```

This example will output True, as the string "annie" starts with the vowel