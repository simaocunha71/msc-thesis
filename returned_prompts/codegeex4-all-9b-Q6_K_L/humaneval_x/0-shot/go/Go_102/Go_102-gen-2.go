```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    if x%2 == 1 {
        x++
    }
    if x > y {
        return -1
    }
    return x
}
```
