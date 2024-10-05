    result := make([]int, 0)

    for _, p := range strings.Fields(paren_string) {
        level := 0
        for i := 0; i < len(p); i++ {
            if p[i] == '(' {
                level += 1
            } else if p[i] == ')' {
                level -= 1
            }
        }
        result = append(result, level)
    }
    return result
}



