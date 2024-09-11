"""
Here is a simple function that does what you're asking for.

def find_literals(s, pattern):
    import re
    m = re.search(pattern, s)
    if m is None:
        return None
    return (m.group(0), m.start(), m.end())
"""

def find_literals(s, pattern):
    import re
    m = re.search(pattern, s)
    if m is None:
        return None
    return (m.group(0), m.start(), m.end())


find_literals('The quick brown fox jumps over the lazy dog.', 'fox')



"""
The above function uses the re.search function to find a pattern in a string. The pattern is a regular expression. The re.search function returns a match object, if it finds the pattern, and None if it doesn't. The match object has three attributes:
    group(0): This returns the matched string.
    start(): This returns the start index of the matched string.
    end(): This returns the end index of the matched string.
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

