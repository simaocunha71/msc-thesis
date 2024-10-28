    result := make([]int, 0)
    current_level := 0

    for _, c := range strings.Split(paren_string, " ") {
        current_level = 0
        for _, d := range c {
            if d == '(' {
                current_level += 1
            } else if d == ')' {
                current_level -= 1
            }
        }
        result = append(result, current_level)
    }
    return result
} 





