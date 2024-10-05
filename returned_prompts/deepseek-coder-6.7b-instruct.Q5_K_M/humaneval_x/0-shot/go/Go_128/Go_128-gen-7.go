    if len(arr) == 0 {
        return nil
    }
    
    sum := 0
    prod := 1

    for _, num := range arr {
        if num > 0 {
            prod *= 1
            sum += int(math.Abs(float6Prod(num)))
        } else if num < 0 {
            prod *= -1
            sum += int(math.Abs(float64(num)))
        } else {
            return 0
        }
    }

    return sum * prod
}
```

## Code 2

```go
