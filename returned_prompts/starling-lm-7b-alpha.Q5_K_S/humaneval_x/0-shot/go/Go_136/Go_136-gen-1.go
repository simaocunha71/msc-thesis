
func LargestSmallestIntegers(lst []int) (a, b int) {
    a, b = 0, 0
    foundNeg, foundPos := false, false
    for _, v := range lst {
        if v < 0 {
            if !foundNeg {
                a = v
                foundNeg = true
            } else {
                if v > a {
                    a = v
                }
            }
        } else {
            if !foundPos {
                b = v
                foundPos = true
            } else {
                if v < b {
                    b = v
                }
            }
        }
    }
    return
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
