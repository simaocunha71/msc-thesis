
def total_match(lst1, lst2):
    return lst1 if sum(len(i) for i in lst1) < sum(len(i) for i in lst2) else lst2

# tests
print(total_match([], [])) ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) ➞ ['4']







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
```
```
```
```
```
```
```
```