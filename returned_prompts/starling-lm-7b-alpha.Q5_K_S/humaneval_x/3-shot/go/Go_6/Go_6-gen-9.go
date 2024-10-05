    result := make([]int, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_depth = max(current_depth, current_depth)
        }else if c == ')' {
            current_depth -= 1
        }
        if c == ' ' {
            result = append(result, current_depth)
        }
    }
    return result
}



