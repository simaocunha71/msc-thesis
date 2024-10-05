    var max interface{}
    switch maxType := maxType(a); maxType {
    case int:
        switch maxType := maxType(b); maxType {
        case int:
            if a.(int) > b.(int) {
                return a
            } else if a.(int) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(int) > b.(float64) {
                return a
            } else if a.(int) < b.(float64) {
                return b
            } else {
                return nil
            }
        default:
            return nil
        }
    case float64:
        switch maxType := maxType(b); maxType {
        case int:
            if a.(float64) > float64(b.(int)) {
                return a
            } else if a.(float64) < float64(b.(int)) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(float64) > b.(float64) {
                return a
            } else if a.(float64) < b.(float64) {
                return b
            } else {
                return nil
            }
        default:
            return nil
        }
    case string:
        if strings.Contains(b.(string), ",") {
            bNum, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
        } else {
            bNum := float64(b.(int))
        }
        if a.(string) > b.(string) {
            return a
        } else if a.(string) < b.(string) {
            return b
        } else {
            return nil
        }
    default:
        return nil
    }
}

// helper function
func maxType(a interface{}) type {
    t := reflect.TypeOf(a)
    switch t.Kind() {
    case reflect.Int:
        return int
    case reflect.Float64:
        return float64
    case reflect.String:
        return string
    default:
        return nil
    }
}
func reflect(a interface{}) reflect.Type {
    return reflect.TypeOf(a)
}
}