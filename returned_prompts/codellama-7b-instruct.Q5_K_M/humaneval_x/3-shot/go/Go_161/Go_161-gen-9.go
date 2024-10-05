    result := make([]rune, 0)

    for _, c := range s {
        if c >= 'A' && c <= 'Z' {
            result = append(result, c + 32)
        }else if c >= 'a' && c <= 'z' {
            result = append(result, c - 32)
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}



