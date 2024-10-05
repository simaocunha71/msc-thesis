    aStr := fmt.Sprint(a)
    bStr := fmt.Sprint(b)
    if strings.Contains(aStr, ".") && !strings.Contains(aStr, ",") {
        aStr = strings.Replace(aStr, ".", "", -1)
    }
    if strings.Contains(bStr, ".") && !strings.Contains(bStr, ",") {
        bStr = strings.Replace(bStr, ".", "", -1)
    }
    if strings.Contains(aStr, ",") {
        aStr = strings.Replace(aStr, ",", ".", -1)
    }
    if strings.Contains(bStr, ",") {
        bStr = strings.Replace(bStr, ",", ".", -1)
    }
    aFloat, err := strconv.ParseFloat(aStr, 64)
    if err == nil {
        bFloat, err := strconv.ParseFloat(bStr, 64)
        if err == nil {
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            } else {
                return nil
            }
        }
    }
    aInt, err := strconv.ParseInt(aStr, 10, 64)
    if err == nil {
        bInt, err := strconv.ParseInt(bStr, 10, 64)
        if err == nil {
            if aInt > bInt {
                return a
            } else if aInt < bInt {
                return b
            } else {
                return nil
            }
        }
    }
    aStrInt, _ := strconv.Atoi(aStr)
    bStrInt, _ := strconv.Atoi(bStr)
    if aStrInt > bStrInt {
        return a
    } else if aStrInt < bStrInt {
        return b
    } else {
        return nil
    }
}
































