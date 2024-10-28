    var a_float64, b_float64 float64
    var a_string, b_string string

    switch a.(type) {
    case int:
        a_float64 = float64(a.(int))
    case float64:
        a_float64 = a.(float64)
    case string:
        a_string = a.(string)
        if strings.Contains(a_string, ".") {
            a_float64, _ = strconv.ParseFloat(a_string, 64)
        }else{
            a_float64, _ = strconv.ParseInt(a_string, 10, 64)
        }
    default:
        fmt.Println("Invalid type")
        return nil
    }

    switch b.(type) {
    case int:
        b_float64 = float64(b.(int))
    case float64:
        b_float64 = b.(float64)
    case string:
        b_string = b.(string)
        if strings.Contains(b_string, ".") {
            b_float64, _ = strconv.ParseFloat(b_string, 64)
        }else{
            b_float64, _ = strconv.ParseInt(b_string, 10, 64)
        }
    default:
        fmt.Println("Invalid type")
        return nil
    }

    if a_float64 > b_float64 {
        return a
    }

    if a_float64 < b_float64 {
        return b
    }
    return nil
}



