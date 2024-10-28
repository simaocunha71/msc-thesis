    result := make([]rune, len(s))
    for i, c := range s {
        result[i] = c + 22 * 2
        if result[i] > 'z' {
            result[i] -= 26
        }
    }
    return string(result)
}



