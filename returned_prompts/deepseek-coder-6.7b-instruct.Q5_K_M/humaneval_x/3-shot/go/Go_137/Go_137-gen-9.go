    var max interface{}
    var err error

    switch a := a.(type) {
    case float64:
        switch b := b.(type) {
        case float64:
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        case string:
            b, err := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err != nil {
                fmt.Println(err)
                return nil
            }
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        }
    case string:
        a, err := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
        if err != nil {
            fmt.Println(err)
            return nil
        }
        switch b := b.(type) {
        case float64:
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        case string:
            b, err := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err != nil {
                fmt.Println(err)
                return nil
            }
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        }
    }
    return max
}



