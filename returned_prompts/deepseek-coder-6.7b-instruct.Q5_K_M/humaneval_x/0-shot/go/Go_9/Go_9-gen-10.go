    maxList := make([]int, len(numbers))
    currentMax := math.MinInt64

    for i, num := range numbers {
        if num > currentMax {
            currentMax = num
        }
        maxList[i] = currentMax
    }

    return maxList
}

```

## 4. 

```go
