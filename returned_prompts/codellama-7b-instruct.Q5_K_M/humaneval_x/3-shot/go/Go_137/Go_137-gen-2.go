    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            }else if b.(int) > a.(int) {
                return b
            }else {
                return nil
            }
        case float64:
            return b
        case string:
            return b
        }
    case float64:
        switch b.(type) {
        case int:
            return a
        case float64:
            if a.(float64) > b.(float64) {
                return a
            }else if b.(float64) > a.(float64) {
                return b
            }else {
                return nil
            }
        case string:
            return b
        }
    case string:
        switch b.(type) {
        case int:
            return a
        case float64:
            return a
        case string:
            a_string := strings.Replace(a.(string), ".", "", 1)
            b_string := strings.Replace(b.(string), ".", "", 1)
            a_int, _ := strconv.Atoi(a_string)
            b_int, _ := strconv.Atoi(b_string)
            if a_int > b_int {
                return a
            }else if b_int > a_int {
                return b
            }else {
                return nil
            }
        }
    }
    return nil
}



