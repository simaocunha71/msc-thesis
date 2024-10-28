    words := strings.Split(s, " ")
    result := make([]rune, 0)
    for _, w := range words {
        if len(w) == 0 {
            result = append(result, ' ')
        }else {
            min := 'z'
            for _, c := range w {
                if c < min {
                    min = c
                }
            }
            for _, c := range w {
                if c == min {
                    result = append(result, c)
                }
            }
        }
    }
    return string(result)
}



