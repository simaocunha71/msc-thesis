    m := make(map[int]bool)

B:
    for _, item := range l {
        if _, ok := m[item]; !ok {
            m[item] = true
        }
    }

C:
    result := make([]int, 0, len(m))

D:
    for key := range m {
        result = append(result, key)
    }

E:
    sort.Ints(result)

F:
    return result
}
```

## 2. 제출한 코드

```go
