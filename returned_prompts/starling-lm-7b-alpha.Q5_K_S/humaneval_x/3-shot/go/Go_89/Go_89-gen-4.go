    result := make([]rune, 0)
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, (c+22)%26 + 'a')
        }else if c >= 'A' && c <= 'Z' {
            result = append(result, (c+22)%26 + 'A')
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}



