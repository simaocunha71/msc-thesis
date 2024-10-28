    result := make([]int, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
        }else if c== ')' {
            current_depth -= 1
        }

        if current_depth > *max_depth {
            *max_depth = current_depth
        }
    }
    result = append(result, *max_depth)

    return result
}



