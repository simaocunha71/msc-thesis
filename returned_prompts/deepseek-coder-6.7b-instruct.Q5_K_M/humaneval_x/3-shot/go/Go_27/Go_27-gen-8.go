    result := make([]rune, len(str))

    for i, c := range str {
        if 'a' <= c && c <= 'z' {
            result[i] = c - 'a' + 'A'
        } else if 'A' <= c && c <= 'Z' {
            result[i] = c - 'A' + 'a'
        } else {
            result[i] = c
        }
    }

    return string(result)
}



