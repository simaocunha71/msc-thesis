    if len(dict) == 0 {
        return false
    }
    var all_lower bool
    var all_upper bool

    for _, key := range dict {
        s := strings.ToLower(strconv.FormatInterface(key))
        if s != strings.ToLower(strconv.FormatInterface(key)) {
            all_lower = false
            break
        }
    }
    for _, key := range dict {
        s := strings.ToUpper(strconv.FormatInterface(key))
        if s != strings.ToUpper(strconv.FormatInterface(key)) {
            all_upper = false
            break
        }
    }
    return all_lower || all_upper
}