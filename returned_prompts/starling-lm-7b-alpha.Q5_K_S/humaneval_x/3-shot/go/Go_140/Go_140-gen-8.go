    result := make([]rune, 0)
    current_space_count := 0
    for _, c := range text {
        if c == ' ' {
            current_space_count += 1
            if current_space_count > 2 {
                result = append(result, '-')
                current_space_count = 1
            } else {
                result = append(result, '_')
            }
        } else {
            result = append(result, c)
            current_space_count = 0
        }
    }
    return string(result)
}



