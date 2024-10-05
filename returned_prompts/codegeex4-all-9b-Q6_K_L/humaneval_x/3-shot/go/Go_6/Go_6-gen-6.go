    paren_list := strings.Split(paren_string, " ")

    result := make([]int, 0)

    for _, paren := range paren_list {
        current_depth := 0
        max_depth := 0

        for _, c := range paren {
            if c == '(' {
                current_depth += 1
                if current_depth > max_depth {
                    max_depth = current_depth
                }
            }else if c == ')' {
                current_depth -= 1
            }
        }
        result = append(result, max_depth)
    }
    return result
}



