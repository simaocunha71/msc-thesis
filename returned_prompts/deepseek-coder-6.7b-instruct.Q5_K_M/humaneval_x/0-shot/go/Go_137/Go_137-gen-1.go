    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case int:
            if a > b {
                return a
            } else if a < b {
                return b
            }
        case float64:
            if float64(a) > b {
                return strconv.FormatFloat(b, 'f', 10, 64)
            } else if float64(a) < b {
                return strconv.FormatFloat(b, 'f', 10, 64)
            }
        case string:
            aFloat, _ := strconv.ParseFloat(strings.ReplaceAll(strconv.Itoa(a), ".", ","), 64)
            bFloat, _ := strconv.ParseFloat(strings.ReplaceAll(b, ",", "."), 64)
            return CompareOne(aFloat, bFloat)
        }
    case float64:
        switch b := b.(type) {
        case int:
            bFloat := float64(b)
            if a > bFloat {
                return strconv.FormatFloat(a, 'f', 10, 64)
            } else if a < bFloat {
                return strconv.FormatFloat(bFloat, 'f', 10, 64)
            }
        case float64:
            if a > b {
                return strconv.FormatFloat(a, 'f', 10, 64)
            } else if a < b {
                return strconv.FormatFloat(b, 'f', 10, 64)
            }
        case string:
            bFloat, _ := strconv.ParseFloat(strings.ReplaceAll(b, ",", "."), 64)
            return CompareOne(a, bFloat)
        }
    case string:
        switch b := b.(type) {
        case int:
            aFloat, _ := strconv.ParseFloat(strings.ReplaceAll(a, ",", "."), 64)
            return CompareOne(aFloat, float64(b))
