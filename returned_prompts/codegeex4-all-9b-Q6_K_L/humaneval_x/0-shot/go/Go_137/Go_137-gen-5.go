```go
func CompareOne(a, b interface{}) interface{} {
    var na, nb float64
    var err error
    switch a.(type) {
    case int:
        na = float64(a.(int))
    case float64:
        na = a.(float64)
    case string:
        na, err = strconv.ParseFloat(strings.Replace(a.(string), ",", ".", 1), 64)
        if err != nil {
            return nil
        }
    default:
        return nil
    }
    switch b.(type) {
    case int:
        nb = float64(b.(int))
    case float64:
        nb = b.(float64)
    case string:
        nb, err = strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
        if err != nil {
            return nil
        }
    default:
        return nil
    }
    if na > nb {
        return a
    }
    if na < nb {
        return b
    }
    return nil
}
```