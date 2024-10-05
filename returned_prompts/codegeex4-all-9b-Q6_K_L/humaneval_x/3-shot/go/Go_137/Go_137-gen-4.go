    aFloat, aFloatErr := strconv.ParseFloat(fmt.Sprintf("%v", a), 64)
    bFloat, bFloatErr := strconv.ParseFloat(fmt.Sprintf("%v", b), 64)
    if aFloatErr == nil && bFloatErr == nil {
        if aFloat > bFloat {
            return a
        } else if aFloat < bFloat {
            return b
        } else {
            return nil
        }
    } else {
        aInt, aIntErr := strconv.Atoi(fmt.Sprintf("%v", a))
        bInt, bIntErr := strconv.Atoi(fmt.Sprintf("%v", b))
        if aIntErr == nil && bIntErr == nil {
            if aInt > bInt {
                return a
            } else if aInt < bInt {
                return b
            } else {
                return nil
            }
        } else {
            aString, aStringErr := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", a), ",", ".", -1), 64)
            bString, bStringErr := strconv.ParseFloat(strings.Replace(fmt.Sprintf("%v", b), ",", ".", -1), 64)
            if aStringErr == nil && bStringErr == nil {
                if aString > bString {
                    return a
                } else if aString < bString {
                    return b
                } else {
                    return nil
                }
            } else {
                return nil
            }
        }
    }
}

