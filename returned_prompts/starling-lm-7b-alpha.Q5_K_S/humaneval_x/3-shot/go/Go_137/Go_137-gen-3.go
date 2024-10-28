    if a == b {
        return nil
    }
    if _, ok := a.(float64); ok {
        if _, ok := b.(float64); ok {
            if a.(float64) > b.(float64) {
                return a
            } else {
                return b
            }
        } else if _, ok := b.(string); ok {
            a_f, _ := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", a), ".", "", -1), 64)
            return a_f > b.(string) {
                return a
            } else {
                return b
            }
        } else {
            return b
        }
    } else if _, ok := a.(string); ok {
        a_f, _ := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", a), ".", "", -1), 64)
        if _, ok := b.(float64); ok {
            return a_f > b.(float64) {
                return a
            } else if _, ok := b.(string); ok {
                b_f, _ := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", b), ".", "", -1), 64)
                if a_f > b_f {
                    return a
                } else {
                    return b
                }
            } else {
                return b
            }
        } else if _, ok := b.(string); ok {
            b_f, _ := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", b), ".", "", -1), 64)
            if a_f > b_f {
                return a
            } else {
                return b
            }
        } else {
            return a
        }
    }
}



