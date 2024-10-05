    var max interface{}
    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case int:
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        case float64:
            if float64(a) > b {
                max = float64(a)
            } else if float64(a) == b {
                max = nil
            } else {
                max = b
            }
        case string:
            aFloat, err := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            if err != nil {
                return err
            }
            bFloat, err := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", b), ",", ".", -1), 64)
            if err != nil {
                return err
            }
            return CompareOne(aFloat, bFloat)
        }
    case float64:
        switch b := b.(type) {
        case int:
            bFloat := float64(b)
            if a > bFloat {
                max = a
            } else if a == bFloat {
                max = nil
            } else {
                max = bFloat
            }
        case float64:
            if a > b {
                max = a
            } else if a == b {
                max = nil
            } else {
                max = b
            }
        case string:
            aFloat := a
            bFloat, err := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err != nil {
                return err
            }
            return CompareOne(aFloat, bFloat)
        }
    case string:
        aFloat, err := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
        if err != nil {
            return err
        }
        switch b := b.(