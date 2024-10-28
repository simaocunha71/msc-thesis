    switch a.(type) {
        case int:
            switch b.(type) {
                case int:
                    if a.(int) > b.(int) {
                        return a
                    }
                case float64:
                    if a.(int) > int(b.(float64)) {
                        return a
                    }
                case string:
                    if a.(int) > strToInt(b.(string)) {
                        return a
                    }
                default:
                    fmt.Println("Wrong type")
            }
        case float64:
            switch b.(type) {
                case int:
                    if a.(float64) > float64(b.(int)) {
                        return a
                    }
                case float64:
                    if a.(float64) > b.(float64) {
                        return a
                    }
                case string:
                    if a.(float64) > strToFloat(b.(string)) {
                        return a
                    }
                default:
                    fmt.Println("Wrong type")
            }
        case string:
            switch b.(type) {
                case int:
                    if strToInt(a.(string)) > b.(int) {
                        return a
                    }
                case float64:
                    if strToFloat(a.(string)) > b.(float64) {
                        return a
                    }
                case string:
                    if a.(string) > b.(string) {
                        return a
                    }
                default:
                    fmt.Println("Wrong type")
            }
        default:
            fmt.Println("Wrong type")
    }
    return nil
}

func strToInt(s string) int {
    s = strings.ReplaceAll(s, ",", "")
    i, err := strconv.Atoi(s)
    if err != nil {
        fmt.Println(err)
    }
    return i
}

func strToFloat(s string) float64 {
    s = strings.ReplaceAll(s,