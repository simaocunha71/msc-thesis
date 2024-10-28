    var a_type, b_type string
    if _, ok := a.(float64); ok {
        a_type = "f"
    }else if _, ok := a.(int); ok {
        a_type = "i"
    }else if _, ok := a.(string); ok {
        a_type = "s"
    }else {
        return nil
    }

    if _, ok := b.(float64); ok {
        b_type = "f"
    }else if _, ok := b.(int); ok {
        b_type = "i"
    }else if _, ok := b.(string); ok {
        b_type = "s"
    }else {
        return nil
    }

    if a_type == "f" && b_type == "i" {
        if a.(float64) > b.(int) {
            return a
        }else if a.(float64) < b.(int) {
            return b
        }else {
            return nil
        }
    }else if a_type == "i" && b_type == "f" {
        if a.(int) > b.(float64) {
            return a
        }else if a.(int) < b.(float64) {
            return b
        }else {
            return nil
        }
    }else if a_type == "s" && b_type == "f" {
        float_a, _ := strconv.ParseFloat(a.(string), 64)
        if float_a > b.(float64) {
            return a
        }else if float_a < b.(float64) {
            return b
        }else {
            return nil
        }
    }else if a_type == "f" && b_type == "s" {
        float_b, _ := strconv.ParseFloat(b.(string), 64)
        if float_a > float_b {
            return a
        }else if float_a < float_b {
            return b
        }else {
            return nil
        }
    }else if a_type == "i" && b