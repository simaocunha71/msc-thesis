```go
func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        return ""
    }
    if x < 0 {
        x = -x
        return "-" + ChangeBase(x, base)
    }
    if x < base {
        return strconv.Itoa(x)
    }
    return ChangeBase(x/base, base) + strconv.Itoa(x%base)
}
```
