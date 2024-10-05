    var a_value, b_value float64
    var err error

    switch a := a.(type) {
    case float64:
        a_value = a
    case string:
        a_value, err = strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
        if err != nil {
            return nil
        }
    case int:
        a_value = float64(a)
    }

    switch b := b.(type) {
    case float64:
        b_value = b
    case string:
        b_value, err = strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
        if err != nil {
            return nil
        }
    case int:
        b_value = float64(b)
    }

    if a_value > b_value {
        return a
    } else if a_value < b_value {
        return b
    } else {
        return nil
    }
}



