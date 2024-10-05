```go
func WillItFly(q []int,w int) bool {
    sum := 0
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
        sum += q[i]
    }
    return sum <= w
}
```
