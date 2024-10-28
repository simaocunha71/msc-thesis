    var a_float float64
    var b_float float64
    var err error

    switch a.(type) {
    case int:
        a_float = float64(a.(int))
    case float64:
        a_float = a.(float64)
    case string:
        a_float, err = strconv.ParseFloat(strings.Replace(a.(string), ",", ".", 1), 64)
        if err != nil {
            return nil
        }
    default:
        return nil
    }

    switch b.(type) {
    case int:
        b_float = float64(b.(int))
    case float64:
        b_float = b.(float64)
    case string:
        b_float, err = strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
        if err != nil {
            return nil
        }
    default:
        return nil
    }

    if a_float == b_float {
        return nil
    }else if a_float > b_float {
        return a
    }else{
        return b
    }
}



