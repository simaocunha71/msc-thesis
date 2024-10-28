    open_brackets_stack := make([]rune, 0)
    for _, c := range brackets {
        if c == '(' {
            open_brackets_stack = append(open_brackets_stack, c)
        } else if c == ')' {
            if len(open_brackets_stack) == 0 {
                return false
            } else {
                open_brackets_stack = open_brackets_stack[:len(open_brackets_stack)-1]
            }
        }
    }
    return len(open_brackets_stack) == 0
}



