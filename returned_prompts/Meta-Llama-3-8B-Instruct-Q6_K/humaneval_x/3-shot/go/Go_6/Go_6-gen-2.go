    result := make([]int, 0)
    current_depth := 0
    for _, c := range strings.Split(paren_string, " ") {
        var depth int
        for _, d := range c {
            if d == '(' {
                current_depth += 1
            } else if d == ')' {
                current_depth -= 1
            }
            depth = current_depth
        }
        result = append(result, depth)
    }
    return result
}