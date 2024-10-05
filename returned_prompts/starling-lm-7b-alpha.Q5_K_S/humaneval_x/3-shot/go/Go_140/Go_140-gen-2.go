    result := make([]rune, 0)
    current_space := false
    for _, c := range text {
        if c == ' ' {
            if current_space {
                result = append(result, '-')
            }else {
                result = append(result, '_')
                current_space = true
            }
        }else {
            result = append(result, c)
            current_space = false
        }
    }
    return string(result)
}



