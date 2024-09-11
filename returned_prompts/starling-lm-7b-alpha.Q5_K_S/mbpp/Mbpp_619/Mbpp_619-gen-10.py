def move_num(s):
    s=list(s)
    s.sort(key=str.isdigit)
    for i in range(len(s)):
        if s[i]=='1' or s[i]=='2' or s[i]=='3' or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9' or s[i]=='0':
            s[i]=s[i]+s[len(s)-i-1]
            del(s[len(s)-i-1])
    return (''.join(s))
move_num('I1love143you55three3000thousand')





"""
Correct Solution:
"""
def move_num(s):
    s = "".join(s)
    s = s.split()
    s = "".join(s)
    return "".join(i for i in s if not i.isdigit()) + "".join(i for i in s if i.isdigit())
print(move_num('I1love143you55three3000thousand'))

# Another Solution:
def move_num(s):
    res = ""
    for c in s:
        if c.isalpha():
            res += c
        else:
            res += c + s.join(s.split(c))
    return res
print(move_num("I1love143you55three3000thousand"))

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

