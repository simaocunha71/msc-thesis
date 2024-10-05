    result := make([]rune, 0)
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            c += 2 * 2
            if c > 'z' {
                c -= 26
            }
        }else if c >= 'A' && c <= 'Z' {
            c += 2 * 2
            if c > 'Z' {
                c -= 26
            }
        }
        result = append(result, c)
    }
    return string(result)
}




