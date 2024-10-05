
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), -x))

# or this, but it's slower
def sort_array_slow(arr):
    return sorted(arr, key=lambda x: (format(x, 'b').count('1'), -x))

# or this, but it's slower
def sort_array_slow2(arr):
    return sorted(arr, key=lambda x: (len(bin(x)) - bin(x).count('1'), -x))


def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), -x))





























```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

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