```go
func MaxElement(l []int) int {
    var max int
    for _, i := range l {
        if i > max {
            max = i
        }
    }
    return max
}
```
