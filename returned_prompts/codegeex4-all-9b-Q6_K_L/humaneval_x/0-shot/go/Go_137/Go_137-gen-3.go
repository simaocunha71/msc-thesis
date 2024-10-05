```go
func CompareOne(a, b interface{}) interface{} {
    var aFloat float64
    var bFloat float64
    switch a.(type) {
    case float64:
        aFloat = a.(float64)
    case int:
        aFloat = float64(a.(int))
    case string:
        aFloat, _ = strconv.ParseFloat(strings.ReplaceAll(a.(string), ",", "."), 64)
    }
    switch b.(type) {
    case float64:
        bFloat = b.(float64)
    case int:
        bFloat = float64(b.(int))
    case string:
        bFloat, _ = strconv.ParseFloat(strings.ReplaceAll(b.(string), ",", "."), 64)
    }
    if aFloat > bFloat {
        return a
    } else if aFloat < bFloat {
        return b
    }
    return nil
}
```