    if a == b {
        return nil
    }

    var float_a float64
    var float_b float64

    switch a.(type) {
    case int:
        float_a = float64(a.(int))
    case float64:
        float_a = a.(float64)
    case string:
        float_a, _ = strconv.ParseFloat(a.(string), 64)
    }

    switch b.(type) {
    case int:
        float_b = float64(b.(int))
    case float64:
        float_b = b.(float64)
    case string:
        float_b, _ = strconv.ParseFloat(b.(string), 64)
    }

    if float_a > float_b {
        return a
    } else {
        return b
    }
}



