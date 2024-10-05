```go
func WillItFly(q []int,w int) bool {
    if len(q) == 0 || w == 0 {
        return false
    }

    sum := 0
    for _, num := range q {
        sum += num
    }

    if sum > w {
        return false
    }

    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-i-1] {
            return false
        }
    }

    return true
}
```
