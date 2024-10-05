    switch aType := a.(type); aType {
    case int:
        switch bType := b.(type) {
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
                return b
            } else {
                return a
            }
        case string:
            if a.(int) > parseFloat(b) {
                return b
            } else {
                return a
            }
        }
    case float64:
        switch bType := b.(type) {
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
            if a > parseFloat(b) {
                return b
            } else {
                return a
            }
        }
    case string:
        switch bType := b.(type) {
        case int:
            if parseFloat(a) > b.(int) {
                return b
            } else {
                return a
            }
        case float64:
            if parseFloat(a) > b {
                return b
            } else {
                return a
            }
        case string:
            if compareStrings(a, b) > 0 {
                return b
            } else {
                return a
            }
        }
    }

    return a
}

func parseFloat(s string) float64 {
    if strings.Contains(s, ",") {
        s = strings.Replace(s, ",", ".", -1)
    }
    return strconv.ParseFloat(s, 64)
}

func compareStrings(a, b string) int {
    if parseFloat(a) > parseFloat(b) {
        return 1
    } else if parseFloat(a) < parseFloat(b) {
        return -1
    } else {
        return 0
    }
}
}  //  end of CompareOne function definition



