```go
func CompareOne(a, b interface{}) interface{} {
    var numA, numB float64
    var errA, errB error

    switch a.(type) {
    case float64:
        numA = a.(float64)
    case string:
        numA, errA = strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
    default:
        return nil
    }

    switch b.(type) {
    case float64:
        numB = b.(float64)
    case string:
        numB, errB = strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
    default:
        return nil
    }

    if errA != nil || errB != nil {
        return nil
    }

    if numA == numB {
        return nil
    } else if numA > numB {
        return a
    } else {
        return b
    }
}
```
