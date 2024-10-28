```go
func WillItFly(q []int, w int) bool {
    if len(q) == 0 || q[0] > w {
        return false
    }
    if len(q) == 1 {
        return true
    }
    if q[0] == q[len(q)-1] && WillItFly(q[1:len(q)-1], w) {
        return true
    }
    if q[0]+q[len(q)-1] > w {
        return false
    }
    return WillItFly(q[1:len(q)-1], w)
}
```
