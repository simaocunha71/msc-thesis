
func LargestSmallestIntegers(lst []int) [2]interface{}{
    smallest, largest := 0, 0
    hasSmall, hasLarge := false, false
    for _, v := range lst {
        if v < 0 {
            if !hasSmall {
                smallest = v
                hasSmall = true
            }
        } else if v > 0 {
            if !hasLarge {
                largest = v
                hasLarge = true
            }
        }
    }
    return [2]interface{}{
        hasSmall && smallest != 0 ? smallest : nil,
        hasLarge && largest != 0 ? largest : nil,
    }
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
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
