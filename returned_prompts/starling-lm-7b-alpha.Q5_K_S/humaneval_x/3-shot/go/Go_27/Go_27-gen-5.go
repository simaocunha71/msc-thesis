    result := make([]rune, len(str))
    for index, c := range str {
        if c >= 'a' && c <= 'z' {
            result[index] = c - 'a' + 'A'
        } else if c >= 'A' && c <= 'Z' {
            result[index] = c - 'A' + 'a'
        } else {
            result[index] = c
        }
    }
    return string(result)
}



