    result := make([]int, 0)
    current_depth := 0
    temp := 0

    for _, c := range strings.Split(paren_string, " ") {
        for _, d := range c {
            if d == '(' {
                current_depth += 1
                temp += 1
            }else if d == ')' {
                current_depth -= 1
            }
        }
        result = append(result, current_depth)
        current_depth = 0
        temp = 0
    }
    return result
}  // 1 1 0 1 1 0 1 1 0 1 0
    // 1 1 2 1 1 0 1 2 1 1 0
    // 1 1 2 1 0 1 1 2 0 1 0
    // 1 1 2 1 1 2 0 1 1 0 0
    // 1 2 0 1 0 1 1 1 0 1 0
    // 1 2 1 1 1 0 1 1 1 0 0
    // 1 2 1 1 1 1 1 1 0 1 0
    // 1 2 1 1 1 1 0 1 1 1 0
    // 1 2 1 1 1 1 1 0 1 1 0
    // 1 2 1 1 1 1 1 1 1 0 0
    // 1 2 1 1 1 1 1 1 1 1 0
    // 1 2 1 1 1 1 1 1 1 1 1
    // 1 2 1 1 1 1 1 1 1 1 2
    // 1 2 1 1 1 1 1 1 1 2 2
    // 1 2 1 1 1 1 1 1 2 2 2
    // 1 2 1 1 1 1 1 2 2 2 2
