    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case int:
            if a > b {
                return a
            }
            if a == b {
                return nil
            }
            return b
        case float64:
            if float64(a) > b {
                return float64(a)
            }
            if float64(a) == b {
                return nil
            }
            return b
        case string:
            aFloat, _ := strconv.ParseFloat(strings.Replace(strconv.Itoa(a), ".", "", 1), 64)
            bFloat, _ := strconv.ParseFloat(strings.Replace(b, ".", "", 1), 64)
            return compareFloat(aFloat, bFloat)
        }
    case float64:
        switch b := b.(type) {
        case int:
            if a > float64(b) {
                return a
            }
            if a == float64(b) {
                return nil
            }
            return float64(b)
        case float64:
            return compareFloat(a, b)
        case string:
            aFloat, _ := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%.2f", a), ".", "", 1), 64)
            bFloat, _ := strconv.ParseFloat(strings.Replace(b, ".", "", 1), 64)
            return compareFloat(aFloat, bFloat)
        }
    case string:
        switch b := b.(type) {
        case int:
            aFloat, _ := strconv.ParseFloat(strings.Replace(a, ".", "", 1), 64)
            return compareFloat(aFloat, float64(b))
        case float64:
            aFloat, _ := strconv.ParseFloat(strings.Replace(a, ".", "", 1), 64)
            return compareFloat(aFloat, b)
        case string:
            aFloat, _ := strconv.Parse