    var a_type, b_type string
    if a_type, _ = strconv.ParseFloat(fmt.Sprint(a), 64); a_type == "" {
        a_type = "int"
    }
    if b_type, _ = strconv.ParseFloat(fmt.Sprint(b), 64); b_type == "" {
        b_type = "int"
    }
    if a_type == "int" {
        if b_type == "float" {
            return b
        }
        if b_type == "string" {
            if strings.Index(b.(string), ".") == 0 && strings.Index(b.(string), ",") == -1 {
                return b
            }
        }
        if a == b {
            return nil
        }
        if b.(float64) > a.(int) {
            return b
        }
    } else {
        if b_type == "int" {
            return a
        }
        if b_type == "string" {
            if strings.Index(b.(string), ".") == 0 && strings.Index(b.(string), ",") == -1 {
                return a
            }
        }
        if a.(float64) > b.(float64) {
            return a
        }
    }
    return nil
}



