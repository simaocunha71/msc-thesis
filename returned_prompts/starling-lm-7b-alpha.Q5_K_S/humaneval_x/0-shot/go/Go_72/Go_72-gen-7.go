
func WillItFly(q []int, w int) bool {
    // Check if the list is palindromic
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    // Calculate the sum of the list
    sum := 0
    for _, v := range q {
        sum += v
    }
    // Return true if the sum is less than or equal to the maximum possible weight, and false otherwise
    return sum <= w
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

