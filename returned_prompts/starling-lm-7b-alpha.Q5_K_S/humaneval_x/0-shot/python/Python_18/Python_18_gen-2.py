

def how_many_times(string: str, substring: str) -> int:
    count = 0
    while True:
        if string.find(substring) == -1:
            break
        string = string[string.find(substring)+1:]
        count += 1
    return count


# Other correct solutions:

def how_many_times(string: str, substring: str) -> int:
    return len(string) - len(string.replace(substring, ''))



```



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```