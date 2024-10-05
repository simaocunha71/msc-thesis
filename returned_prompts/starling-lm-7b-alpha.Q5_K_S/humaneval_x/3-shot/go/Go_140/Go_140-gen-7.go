    result := make([]rune, 0)

    for _, c := range text {
        if c == ' ' {
            if len(result) > 0 && result[len(result)-1] == '_' {
                result = append(result, '-')
            }else {
                result = append(result, '_')
            }
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}




