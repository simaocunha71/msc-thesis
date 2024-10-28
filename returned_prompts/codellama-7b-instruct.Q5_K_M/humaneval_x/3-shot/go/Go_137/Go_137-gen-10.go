    switch a.(type) {
        case int:
            switch b.(type) {
                case int:
                    if a.(int) > b.(int) {
                        return a
                    }else if a.(int) < b.(int) {
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
                    }else if a.(float64) < b.(float64) {
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
                    a_str := strings.ReplaceAll(a.(string), ",", ".")
                    b_str := strings.ReplaceAll(b.(string), ",", ".")

                    a_num, _ := strconv.ParseFloat(a_str, 64)
                    b_num, _ := strconv.ParseFloat(b_str, 64)

                    if a_num > b_num {
                        return a
                    }else if a_num < b_num {
                        return b
                    }else {
                        return nil
                    }
            }
    }
    return nil
}



