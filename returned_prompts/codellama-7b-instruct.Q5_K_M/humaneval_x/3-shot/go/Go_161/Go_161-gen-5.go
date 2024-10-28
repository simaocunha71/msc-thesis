    result := make([]byte, 0, len(s))
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, byte(c-32))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, byte(c+32))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}



