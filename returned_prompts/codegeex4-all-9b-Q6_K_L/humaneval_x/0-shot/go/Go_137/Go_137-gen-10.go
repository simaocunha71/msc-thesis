```go
func CompareOne(a, b interface{}) interface{} {
    switch at := a.(type) {
    case int:
        switch bt := b.(type) {
        case int:
            if at == bt {
                return nil
            }
            if at > bt {
                return a
            }
            return b
        case float64:
            if float64(at) == bt {
                return nil
            }
            if float64(at) > bt {
                return a
            }
            return b
        case string:
            if f, err := strconv.ParseFloat(strings.ReplaceAll(bt, ",", "."), 64); err == nil {
                if float64(at) == f {
                    return nil
                }
                if float64(at) > f {
                    return a
                }
                return b
            }
        }
    case float64:
        switch bt := b.(type) {
        case int:
            if at == float64(bt) {
                return nil
            }
            if at > float64(bt) {
                return a
            }
            return b
        case float64:
            if at == bt {
                return nil
            }
            if at > bt {
                return a
            }
            return b
        case string:
            if f, err := strconv.ParseFloat(strings.ReplaceAll(bt, ",", "."), 64); err == nil {
                if at == f {
                    return nil
                }
                if at > f {
                    return a
                }
                return b
            }
        }
    case string:
        switch bt := b.(type) {
        case int:
            if f, err := strconv.ParseFloat(strings.ReplaceAll(at, ",", "."), 64); err == nil {
                if f == float64(bt) {
                    return nil
                }
                if f > float64(bt) {
                    return a
                }
                return b
            }
        case float64:
            if f, err := strconv.ParseFloat(strings.ReplaceAll(at, ",", "."), 64); err == nil {
                if f == bt {
                    return nil
                }
                if f > bt {
                    return a
                }
                return b
            }
        case string:
            if fa, err := strconv.ParseFloat(strings.ReplaceAll(at, ",", "."), 64); err == nil {
                if fb, err := strconv.ParseFloat(strings.ReplaceAll(bt, ",", "."), 64); err == nil {
                    if fa == fb {
