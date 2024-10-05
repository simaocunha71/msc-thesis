    var res []int

    for _, v := range values {
        if val, ok := v.(int); ok {
            res = append(res, val)
        }
    }

    return res
}

```

## Task 2

```go
