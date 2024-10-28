    if a == b {
        return nil
    }

    switch a := a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a > b {
                return a
            } else {
                return b
            }
        case float64:
            if a > b {
                return a
            } else {
                return b
            }
        case string:
            if _, err := strconv.ParseFloat(b.(string)); err != nil {
                return a
            } else {
                if a > b {
                    return a
                } else {
                    return b
                }
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a > b {
                return a
            } else {
                return b
            }
        case float64:
            if a > b {
                return a
            } else {
                return b
            }
        case string:
            if _, err := strconv.ParseFloat(b.(string)); err != nil {
                return a
            } else {
                if a > b {
                    return a
                } else {
                    return b
                }
            }
        }
    case string:
        switch b.(type) {
        case int:
            if _, err := strconv.Atoi(a.(string)); err != nil {
                return b
            } else {
                if a > b {
                    return a
                } else {
                    return b
                }
            }
        case float64:
            if _, err := strconv.ParseFloat(a.(string)); err != nil {
                return b
            } else {
                if a > b {
                    return a
                } else {
                    return b
                }
            }
        case string:
            if a > b {
                return a
            } else {
                return b
            }
        }
    }

    return nil
}

func main() {
