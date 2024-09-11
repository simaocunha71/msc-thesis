def removezero_ip(ip):
    ip = ip.split('.')
    for i in range(len(ip)):
        if len(ip[i]) == 0:
            ip[i] = '0'
    return ".".join(ip)

# Another way
"""
def removezero_ip(ip):
    return ".".join(i if i else '0' for i in ip.split('.'))
"""


# Test
print(removezero_ip("216.08.094.196"))


"""
Explanation:
We can split the ip address string into four parts by splitting the string at the '.' character.
Then we check if the ith part of the ip address is empty. If it is, then we assign '0' to it.
Finally, we join the ip address parts with '.' character to form a valid ip address.
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