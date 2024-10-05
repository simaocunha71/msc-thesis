    if a == b {
        return nil
    }else if a, ok := a.(string); ok {
        if _, ok := b.(string); ok {
            a, err := strconv.ParseFloat(a, 64)
            if err != nil {
                return a
            }
            b, err := strconv.ParseFloat(b, 64)
            if err != nil {
                return b
            }
        } else {
            a, _ := strconv.ParseFloat(a, 64)
            return a
        }
    } else if _, ok := b.(string); ok {
        b, _ := strconv.ParseFloat(b, 64)
        return b
    }

    if a > b {
        return a
    } else {
        return b
    }
}



