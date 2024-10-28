    switch a.(type) {
    case float64:
        af := a.(float64)
        switch b.(type) {
        case float64:
            bf := b.(float64)
            if af > bf {
                return af
            } else if af < bf {
                return bf
            }
        case string:
            bs := b.(string)
            bs = strings.Replace(bs, ",", ".", -1)
            bsf, _ := strconv.ParseFloat(bs, 64)
            if af > bsf {
                return af
            } else if af < bsf {
                return bsf
            }
        }
    case string:
        as := a.(string)
        as = strings.Replace(as, ",", ".", -1)
        af, _ := strconv.ParseFloat(as, 64)
        switch b.(type) {
        case float64:
            if af > b.(float64) {
                return af
            } else if af < b.(float64) {
                return b.(float64)
            }
        case string:
            bs := b.(string)
            bs = strings.Replace(bs, ",", ".", -1)
            bsf, _ := strconv.ParseFloat(bs, 64)
            if af > bsf {
                return af
            } else if af < bsf {
                return bsf
            }
        }
    case int:
        if a.(int) > b.(int) {
            return a
        } else if a.(int) < b.(int) {
            return b
        }
    }
    return nil
}


A: This solution works by first checking the type of the inputs a and b. If a or b is a float64, it converts the other argument (if it is a string, it converts it to a float64) and compares them. If a or b is a string, it converts it to a float64 and compares it to the other argument. If a or b is an integer, it compares them directly.