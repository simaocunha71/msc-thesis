    var result interface{}
    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case int:
            if a>b {
                result = a
            } else if a == b {
                result = nil
            } else {
                result = b
            }
        case float64:
            if float64(a)>b {
                result = b
            } else if float64(a) == b {
                result = nil
            } else {
                result = b
            }
        case string:
            a_float, err := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            if err != nil {
                return err
            }
            b_float, err := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", b), ",", ".", -1), 64)
            if err != nil {
                return err
            }
            return CompareOne(a_float, b_float)
        }
    case float64:
        switch b := b.(type) {
        case int:
            result = CompareOne(b, a)
        case float64:
            if a>b {
                result = a
            } else if a == b {
                result = nil
            } else {
                result = b
            }
        case string:
            a_float, err := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%.2f", a), ",", ".", -1), 64)
            if err != nil {
                return err
            }
            b_float, err := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err != nil {
                return err
            }
            return CompareOne(a_float, b_float)
        }
    case string:
        switch b := b.(type) {
        case int:
            result = CompareOne(b, a)
        case float64:
            result = CompareOne(a, b)