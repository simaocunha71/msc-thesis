    var result []rune
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, c + 2)
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, c + 2)
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}



