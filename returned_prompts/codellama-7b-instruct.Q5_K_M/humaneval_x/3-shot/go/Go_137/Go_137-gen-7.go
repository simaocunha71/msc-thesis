    switch a.(type) {
        case int:
            if b.(float64) > float64(a.(int)) {
                return b
            }
            if b.(float64) < float64(a.(int)) {
                return a
            }
            return nil
        case float64:
            if b.(float64) > a.(float64) {
                return b
            }
            if b.(float64) < a.(float64) {
                return a
            }
            return nil
        case string:
            // Convert strings to floats
            a_float, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
            b_float, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)

            // Compare floats
            if b_float > a_float {
                return b
            }
            if b_float < a_float {
                return a
            }
            return nil
    }
    return nil
}



