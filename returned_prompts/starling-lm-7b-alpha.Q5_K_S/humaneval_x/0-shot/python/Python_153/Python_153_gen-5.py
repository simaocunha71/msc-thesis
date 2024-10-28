
def Strongest_Extension(class_name, extensions):
    strengths = []
    strongest = ''
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        small = sum(1 for c in extension if c.islower())
        strength = cap - small
        strengths.append((strength, extension))
    strengths.sort()
    return '.'.join([class_name] + strongest[1:])


































```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
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