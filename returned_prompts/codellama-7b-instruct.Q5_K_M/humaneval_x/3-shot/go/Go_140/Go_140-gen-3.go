    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range text {
        if c == ' ' {
            current_depth += 1
            current_string = append(current_string, '_')
        }else{
            current_depth = 0
            current_string = append(current_string, c)
        }

        if current_depth == 2{
            result = append(result, string(current_string))
            current_string = make([]rune, 0)
        }
    }
    return strings.Join(result, "_")
}



