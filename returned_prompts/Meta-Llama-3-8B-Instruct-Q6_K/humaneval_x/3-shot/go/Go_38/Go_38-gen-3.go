    result := make([]rune, 0)
    for i := 0; i < len(s); i += 3 {
        group := s[i:i+3]
        result = append(result, group[2], group[0])
    }
    return string(result)
}