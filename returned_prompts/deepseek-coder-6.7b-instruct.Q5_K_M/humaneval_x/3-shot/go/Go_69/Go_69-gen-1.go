    frequency := make(map[int]int)

    for _, num := range lst {
        frequency[num]++
    }

    for i := len(lst) - 1; i >= 0; i-- {
        if frequency[lst[i]] > lst[i] {
            return lst[i]
        }
    }

    return -1
}
```

## 2.2. Problem Solving

```go

