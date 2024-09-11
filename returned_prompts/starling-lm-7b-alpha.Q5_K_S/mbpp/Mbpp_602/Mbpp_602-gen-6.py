from collections import Counter
def first_repeated_char(s:str)->str:
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]]>1 and s.index(s[i])!=i:
            return s[i]
    return "No repeated char"

# Alternative
from collections import defaultdict
def first_repeated_char(s:str)->str:
    c = defaultdict(int)
    for i in range(len(s)):
        c[s[i]]+=1
        if c[s[i]]>1:
            return s[i]
    return "No repeated char"


# Test
print(first_repeated_char("abcabc"))
"""
'a'
"""

# Alternative Test
print(first_repeated_char("abcd"))
"""
'No repeated char'
"""

# Stress Test
for _ in range(100000):
    s = "abcdefghijklmnopqrstuvwxyz"
    print(first_repeated_char(s))
"""
'a'
"""




"""



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