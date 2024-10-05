    var result interface{}
    var aFloat float64
    var bFloat float64
    var aStr string
    var bStr string
    var aInt int
    var bInt int
    var aStrArr []string
    var bStrArr []string
    var aStrArrSplit []string
    var bStrArrSplit []string

    switch a.(type) {
    case int:
        aInt = a.(int)
        if b.(int) > aInt {
            result = b
        } else if b.(int) < aInt {
            result = a
        } else {
            result = nil
        }
    case float64:
        aFloat = a.(float64)
        if b.(float64) > aFloat {
            result = b
        } else if b.(float64) < aFloat {
            result = a
        } else {
            result = nil
        }
    case string:
        aStr = a.(string)
        if b.(string) != "" {
            bStr = b.(string)
        } else {
            return nil
        }
        aStrArr = strings.Split(aStr, ",")
        bStrArr = strings.Split(bStr, ",")
        aStrArrSplit = strings.Split(aStrArr[0], ".")
        bStrArrSplit = strings.Split(bStrArr[0], ".")
        if len(aStrArrSplit) == 2 {
            if aStrArrSplit[1] != "" {
                aFloat, _ := strconv.ParseFloat(aStrArrSplit[1], 64)
                bFloat, _ := strconv.ParseFloat(bStrArrSplit[1], 64)
                if aFloat < bFloat {
                    result = b
                } else if aFloat > bFloat {
                    result = a
                } else {
                    result = nil
                }
            } else {
                if float64(aInt) < float64(bInt) {
                    result = b
                } else if float64(aInt) > float64(bInt) {
