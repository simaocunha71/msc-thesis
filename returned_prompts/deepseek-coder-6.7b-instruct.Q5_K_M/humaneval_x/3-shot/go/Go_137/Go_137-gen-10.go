    var aType = fmt.Sprintf("%T", a)
    var bType = fmt.Sprintf("%T", b)

    switch {
    case aType == "int" && bType == "float64":
        return b
    case aType == "float64" && bType == "int":
        return a
    case aType == "float64" && bType == "float64":
        if a.(float64) > b.(float64) {
            return a
        } else if b.(float64) > a.(float64) {
            return b
        } else {
            return nil
        }
    case aType == "int" && bType == "int":
        if a.(int) > b.(int) {
            return a
        } else if b.(int) > a.(int) {
            return b
        } else {
            return nil
        }
    case aType == "string" && bType == "string":
        aFloat, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
        bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)

        if aFloat > bFloat {
            return a
        } else if bFloat > aFloat {
            return b
        } else {
            return nil
        }
    case aType == "string" && bType == "int":
        aFloat, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
        return aFloat > float64(b.(int))
    case aType == "int" && bType == "string":
        bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
        return float64(a.(int)) > bFloat
    case aType == "string" && bType == "float64":
        aFloat, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -