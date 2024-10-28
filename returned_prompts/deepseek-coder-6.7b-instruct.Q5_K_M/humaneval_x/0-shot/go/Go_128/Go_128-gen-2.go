    if len(arr) == 0 {
        return nil
    }
    sum := 0
    prod := 1
    for _, val := range arr {
        if val > 0 {
            prod *= 1
        } else if val < 0 {
            prod *= -1
        } else {
            return 0
        }
        sum += int(math.Abs(float64(val)))
    }
    return sum * prod
}

```

## 5. 

```go
