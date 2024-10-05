def total_match(lst1, lst2):
    l1 = 0
    for i in lst1:
        l1 += len(i)
    l2 = 0
    for i in lst2:
        l2 += len(i)
    if l1 == l2:
        return lst1
    elif l1 < l2:
        return lst1
    else:
        return lst2

# testing the function
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ['4']
print(total_match(['a', 'bb', 'ccc', 'dd'], ['aa', 'bbb', 'cccc', 'ddd']))  # ['aa', 'bbb', 'cccc', 'ddd']
print(total_match(['cat'], []))  # []
print(total_match(['dog'], ['cat', 'cow', 'dog']))  # ['cat', 'cow', 'dog']






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
``