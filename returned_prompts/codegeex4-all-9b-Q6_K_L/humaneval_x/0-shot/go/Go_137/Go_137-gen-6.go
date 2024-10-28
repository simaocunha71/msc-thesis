```go
func CompareOne(a, b interface{}) interface{} {
    if a == b {
        return nil
    }
    switch a.(type) {
    case int:
        if b, ok := b.(int); ok {
            if a.(int) > b {
                return a
            } else {
                return b
            }
        }
    case float64:
        if b, ok := b.(float64); ok {
            if a.(float64) > b {
                return a
            } else {
                return b
            }
        }
    case string:
        if b, ok := b.(string); ok {
            fa, err1 := strconv.ParseFloat(strings.ReplaceAll(a.(string), ",", "."), 64)
            fb, err2 := strconv.ParseFloat(strings.ReplaceAll(b.(string), ",", "."), 64)
            if err1 != nil || err2 != nil {
                return nil
            }
            if fa > fb {
                return a
            } else {
                return b
            }
        }
    }
    return nil
}
```