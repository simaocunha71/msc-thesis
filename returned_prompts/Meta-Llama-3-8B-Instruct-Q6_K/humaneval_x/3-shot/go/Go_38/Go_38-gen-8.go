    result := make([]byte, 0)
    for i := 0; i < len(s); i += 2 {
        result = append(result, s[i])
        if i+1 < len(s) {
            result = append(result, s[i+1])
        }
    }
    return string(result)
}