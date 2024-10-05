```go
func GetPositive(l []int) []int {
    var ret []int
    for _, n := range l {
        if n > 0 {
            ret = append(ret, n)
        }
    }
    return ret
}
```