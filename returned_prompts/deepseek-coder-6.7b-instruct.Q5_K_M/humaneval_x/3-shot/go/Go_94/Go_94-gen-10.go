    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth  := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_