    result := make([]rune, 0)
    for _, r := range str {
        if r >= 'a' && r <= 'z' {
            result = append(result, r - 'a' + 'A')
        }else if r >= 'A' && r <= 'Z' {
            result = append(result, r - 'A' + 'a')
        }else {
            result = append(result, r)
        }
    }
    return string(result)
}



