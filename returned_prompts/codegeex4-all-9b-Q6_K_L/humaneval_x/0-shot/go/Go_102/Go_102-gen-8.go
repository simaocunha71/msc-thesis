```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    for i := y; i >= x; i-- {
        if i%2 == 0 {
            return i
        }
    }
    return -1
}
```