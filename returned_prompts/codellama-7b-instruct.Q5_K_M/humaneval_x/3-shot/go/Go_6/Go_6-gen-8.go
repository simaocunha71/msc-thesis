    result := make([]int, 0)
    for _, group := range strings.Split(paren_string, " ") {
        current_depth := 0
        for _, c := range group {
            if c == '(' {
                current_depth += 1
            } else if c == ')' {
                current_depth -= 1
            }
        }
        result = append(result, current_depth)
    }
    return result
}



