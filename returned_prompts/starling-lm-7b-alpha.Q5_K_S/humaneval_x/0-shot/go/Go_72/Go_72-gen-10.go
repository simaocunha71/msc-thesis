
func WillItFly(q []int, w int) bool {
    // check if the sum of the elements is less than or equal to the maximum possible weight
    if sum(q) <= w {
        // check if the list is palindromic
        if isPalindromic(q) {
            return true
        }
    }
    return false
}

func sum(s []int) int {
    sum := 0
    for _, v := range s {
        sum += v
    }
    return sum
}

func isPalindromic(s []int) bool {
    l := 0
    r := len(s) - 1
    for l < r {
        if s[l] != s[r] {
            return false
        }
        l++
        r--
    }
    return true
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

``