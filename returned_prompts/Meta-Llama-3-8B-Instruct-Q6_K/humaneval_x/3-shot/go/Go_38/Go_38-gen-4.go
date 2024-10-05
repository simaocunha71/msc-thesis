    result := make([]byte, 0)
    i := 0
    for i < len(s) {
        if i+2 < len(s) {
            result = append(result, s[i+1])
            i += 3
        } else {
            result = append(result, s[i])
            i += 1
        }
    }
    return string(result)
}