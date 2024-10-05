    result := make([]int, 0)
    var max_depth int = 0

    for _, p := range strings.Fields(paren_string) {
        depth := 0
        for _, c := range p {
            if c == '(' {
                depth += 1
            } else if c == ')' {
                depth -= 1
            }
        }
        if depth > max_depth {
            max_depth = depth
        }
        result = append(result, depth)
    }
    return result
}



