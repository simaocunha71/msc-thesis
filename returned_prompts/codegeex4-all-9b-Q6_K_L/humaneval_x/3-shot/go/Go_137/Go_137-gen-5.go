    aFloat, err := strconv.ParseFloat(fmt.Sprintf("%v", a), 64)
    if err != nil {
        return nil
    }
    bFloat, err := strconv.ParseFloat(fmt.Sprintf("%v", b), 64)
    if err != nil {
        return nil
    }

    if aFloat > bFloat {
        return a
    } else if aFloat < bFloat {
        return b
    } else {
        return nil
    }
}



