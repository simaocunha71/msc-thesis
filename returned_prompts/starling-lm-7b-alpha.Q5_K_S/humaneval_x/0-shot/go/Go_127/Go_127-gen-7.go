    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    l := max(interval1[0], interval2[0])
    r := min(interval1[1], interval2[1])
    length := r - l + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func isPrime(n int) bool {
    if n == 2 {
        return true
    }
    if n == 1 || n % 2 == 0 {
        return false
    }
    for i := 3; i*i <= n; i += 2 {
        if n % i == 0 {
            return false
        }
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