    stack := make([]rune, 0)

    for _, c := range brackets {
        switch {
        case c == '(':
            stack = append(stack, c)
        case c == ')':
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}



