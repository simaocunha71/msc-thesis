    stack := make([]rune, 0)
    for _, c := range lst[0] {
        if c == '(' {
            stack = append(stack, '(')
        } else {
            if len(stack) == 0 {
                return "No"
            }
            stack = stack[:len(stack)-1]
        }
    }

    if len(stack) != 0 {
        return "No"
    }

    stack = make([]rune, 0)
    for _, c := range lst[1] {
        if c == ')' {
            stack = append(stack, ')')
        } else {
            if len(stack) == 0 {
                return "No"
            }
            stack = stack[:len(stack)-1]
        }
    }

    if len(stack) != 0 {
        return "No"
    }
    return "Yes"
}



