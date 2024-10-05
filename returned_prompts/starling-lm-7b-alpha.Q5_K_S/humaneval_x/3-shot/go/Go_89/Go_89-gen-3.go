    result := make([]rune, len(s))
    for i, c := range s {
        if c >= 'a' && c <= 'z' {
            result[i] = (c + 2*2) % 26 + 'a'
        }else if c >= 'A' && c <= 'Z' {
            result[i] = (c + 2*2) % 26 + 'A'
        }else {
            result[i] = c
        }
    }
    return string(result)
}



