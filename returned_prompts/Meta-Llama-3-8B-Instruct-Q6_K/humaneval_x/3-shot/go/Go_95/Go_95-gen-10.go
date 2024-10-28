    if len(dict) == 0 {
        return false
    }

    all_lower := true
    all_upper := true

    for _, key := range dict {
        s := strings.ToLower(strconv.FormatInterface(key))
        if s != strings.ToLower(strconv.FormatInterface(key)) {
            all_lower = false
        }
        s = strings.ToUpper(strconv.FormatInterface(key))
        if s != strings.ToUpper(strconv.FormatInterface(key)) {
            all_upper = false
        }
    }

    return all_lower || all_upper
}