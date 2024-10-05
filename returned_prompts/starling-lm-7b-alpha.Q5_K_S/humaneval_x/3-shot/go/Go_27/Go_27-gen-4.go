    result := make([]rune, 0, len(str))
    for _, c := range str {
        if c >= 'a' && c <= 'z' {
            result = append(result, c - 32)
        } else {
            result = append(result, c + 32)
        }
    }
    return string(result)
}



