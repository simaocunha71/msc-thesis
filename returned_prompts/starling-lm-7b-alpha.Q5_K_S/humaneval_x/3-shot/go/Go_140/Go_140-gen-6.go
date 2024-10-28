    var result_string_buffer = make([]rune, 0)
    var consecutive_spaces = 0
    for _, c := range text {
        if c == ' ' {
            consecutive_spaces += 1
            if consecutive_spaces > 2 {
                result_string_buffer = append(result_string_buffer, '-')
                consecutive_spaces = 2
            } else {
                result_string_buffer = append(result_string_buffer, '_')
            }
        } else {
            result_string_buffer = append(result_string_buffer, c)
            consecutive_spaces = 0
        }
    }
    return string(result_string_buffer)
}



