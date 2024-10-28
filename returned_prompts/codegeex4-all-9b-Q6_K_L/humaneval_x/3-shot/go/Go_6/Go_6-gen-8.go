    result := make([]int, 0)
    paren_groups := strings.Split(paren_string, " ")
    current_depth := 0

    for _, group := range paren_groups {
        current_depth = 0
        for _, c := range group {
            if c == '(' {
                current_depth += 1
            }else if c == ')'{
                current_depth -= 1
            }

            if current_depth > 0 {
                result = append(result, current_depth)
            }
        }
    }

    return result
}

