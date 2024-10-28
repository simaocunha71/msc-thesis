
func TotalMatch(lst1 []string, lst2 []string) []string {
    if len(lst1) < len(lst2) {
        return lst1
    }
    if len(lst1) > len(lst2) {
        return lst2
    }
    for _, v1 := range lst1 {
        for _, v2 := range lst2 {
            if len(v1) < len(v2) {
                return lst1
            }
            if len(v1) > len(v2) {
                return lst2
            }
        }
    }
    return lst1
}





```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

