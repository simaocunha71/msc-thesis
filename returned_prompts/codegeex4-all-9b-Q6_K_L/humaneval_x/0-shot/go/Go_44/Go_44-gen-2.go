```go
func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    return strconv.FormatInt(int64(x), base)
}
```