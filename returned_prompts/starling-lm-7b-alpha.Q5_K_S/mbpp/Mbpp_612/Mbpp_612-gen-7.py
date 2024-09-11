```
def merge(lst):
    a = []
    b = []
    for i in lst:
        a.append(i[0])
        b.append(i[1])
    return [a, b]
```

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

def merge(lst):
    a = []
    b = []
    for i in lst:
        a.append(i[0])
        b.append(i[1])
    return [a, b]

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

def merge(lst):
    return [i[0] for i in lst], [i[1] for i in lst]

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

def merge(lst):
    return [i[0] for i in lst], [i[1] for i in lst]

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

def merge(lst):
    return list(map(list, zip(*lst)))

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

def merge(lst):
    return list(map(list, zip(*lst)))

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# ['x', 'a', 'm']
# ['y', 'b', 'n']

```

merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
