```go
func CompareOne(a, b interface{}) interface{} {
    var av, bv float64
    switch a.(type) {
    case int:
        av = float64(a.(int))
    case float64:
        av = a.(float64)
    case string:
        av, _ = strconv.ParseFloat(strings.Replace(a.(string), ",", ".", 1), 64)
    }
    switch b.(type) {
    case int:
        bv = float64(b.(int))
    case float64:
        bv = b.(float64)
    case string:
        bv, _ = strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
    }
    if av > bv {
        return a
    } else if av < bv {
        return b
    }
    return nil
}
```