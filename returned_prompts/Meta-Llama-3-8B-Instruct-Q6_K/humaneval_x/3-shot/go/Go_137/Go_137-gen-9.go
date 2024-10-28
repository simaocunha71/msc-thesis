    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            } else if a.(int) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(int) > b {
                return a
            } else if a.(int) < b {
                return b
            } else {
                return nil
            }
        case string:
            if a.(int) > getFloat(b) {
                return a
            } else if a.(int) < getFloat(b) {
                return b
            } else {
                return nil
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a > b.(int) {
                return a
            } else if a < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a > b {
                return a
            } else if a < b {
                return b
            } else {
                return nil
            }
        case string:
            if a > getFloat(b) {
                return a
            } else if a < getFloat(b) {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            if getFloat(a) > b.(int) {
                return a
            } else if getFloat(a) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if getFloat(a) > b {
                return a
            } else if getFloat(a) < b {
                return b
            } else {
                return nil
            }
        case string:
            if getFloat(a) > getFloat(b) {
                return a
            } else if getFloat(a) < getFloat(b) {
                return b
            } else {
                return nil
            }
        }
    }

    return nil
}

func getFloat(s string) float64 {
    s = strings.Replace(s, ",", ".", -1)
    f, _ := strconv.ParseFloat(s, 64)
    return f
}