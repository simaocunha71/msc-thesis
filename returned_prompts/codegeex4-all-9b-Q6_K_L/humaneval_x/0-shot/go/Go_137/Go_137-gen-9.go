```go
func CompareOne(a, b interface{}) interface{} {
    var aVal, bVal float64
    var err error

    if a, ok := a.(float64); ok {
        aVal = a
    } else if a, ok := a.(string); ok {
        aVal, err = strconv.ParseFloat(strings.ReplaceAll(a, ",", "."), 64)
        if err != nil {
            return nil
        }
    } else {
        return nil
    }

    if b, ok := b.(float64); ok {
        bVal = b
    } else if b, ok := b.(string); ok {
        bVal, err = strconv.ParseFloat(strings.ReplaceAll(b, ",", "."), 64)
        if err != nil {
            return nil
        }
    } else {
        return nil
    }

    if aVal == bVal {
        return nil
    } else if aVal > bVal {
        return a
    } else {
        return b
    }
}
```
