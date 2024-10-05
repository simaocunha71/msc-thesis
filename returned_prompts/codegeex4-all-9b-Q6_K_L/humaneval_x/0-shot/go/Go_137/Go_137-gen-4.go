```go
func CompareOne(a, b interface{}) interface{} {
    af, _ := strconv.ParseFloat(fmt.Sprintf("%v", a), 64)
    bf, _ := strconv.ParseFloat(fmt.Sprintf("%v", b), 64)
    if af > bf {
        return a
    }
    if af < bf {
        return b
    }
    return nil
}
```