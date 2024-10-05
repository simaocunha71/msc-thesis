    result := make([]byte, 0)
    for _, c := range s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            if 'a' <= c && c <= 'z' {
                result = append(result, byte(c-'a'+65))
            } else {
                result = append(result, byte(c-'A'+97))
            }
        } else {
            result = append(result, c)
        }
    }
    if len(result) == 0 {
        result = []byte(s)
        bytes.Reverse(result)
    }
    return string(result)
}