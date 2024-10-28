    result := make([]int, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
        }else if c== ')' {
            current_depth -= 1
        }
        if current_depth > result[len(result)-1] {
            result = append(result, current_depth)
        }
    }
    return result
}



