    var a_float float64
    var b_float float64

    switch a.(type) {
    case float64:
        a_float = a.(float64)
    case int:
        a_float = float64(a.(int))
    case string:
        a_float, _ = strconv.ParseFloat(strings.ReplaceAll(a.(string), ",", "."), 64)
    }

    switch b.(type) {
    case float64:
        b_float = b.(float64)
    case int:
        b_float = float64(b.(int))
    case string:
        b_float, _ = strconv.ParseFloat(strings.ReplaceAll(b.(string), ",", "."), 64)
    }

    if a_float == b_float {
        return nil
    } else if a_float > b_float {
        return a
    } else {
        return b
    }
}

