
    var sum int = 0
    for i := 0; i < len(lst); i++ {
        if i % 2 == 0 && lst[i] % 2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}

```

## Solution 2
```go
