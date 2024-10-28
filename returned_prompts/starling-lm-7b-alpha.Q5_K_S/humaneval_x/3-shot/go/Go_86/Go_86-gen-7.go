    words := strings.Split(s, " ")
    result := make([]rune, 0)
    for _, w := range words {
        min_ascii := 'z'
        for _, c := range w {
            if c < min_ascii {
                min_ascii = c
            }
        }
        result = append(result, min_ascii)
        result = append(result, ' ')
    }
    return string(result)
}



