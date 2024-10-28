    result  := make([]string, 0)
    current := make([]rune, 0)
    depth   := 0

    for _, c := range paren_string {
        if c == '(' {
            depth += 1
            current = append(current, c)
        } else if c == ')' {
            depth -= 1
            current = append(current, c)

            if depth == 0 {
                result = append(result, string(current))
                current = make([]rune, 0)
            }
        }
    }

    return result
}



