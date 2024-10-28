    result := make([]rune, 0)
    consecutive_spaces := 0

    for _, c := range text {
        if c == ' ' {
            consecutive_spaces += 1
            if consecutive_spaces > 2 {
                result = append(result, '-')
                consecutive_spaces = 2
            }else {
                result = append(result, '_')
            }
        } else {
            result = append(result, c)
            consecutive_spaces = 0
        }
    }
    return string(result)
}



