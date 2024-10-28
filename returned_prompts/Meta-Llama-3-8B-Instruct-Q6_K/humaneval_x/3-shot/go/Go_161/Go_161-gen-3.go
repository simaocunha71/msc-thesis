    result := make([]byte, 0)
    for _, c := range s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            if c <= 'z' {
                result = append(result, byte(c-'a'+ 'A'))
            } else {
                result = append(result, byte(c-'A'+ 'a'))
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}