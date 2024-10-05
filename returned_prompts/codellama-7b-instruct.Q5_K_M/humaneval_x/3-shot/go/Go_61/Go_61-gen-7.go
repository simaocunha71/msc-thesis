    stack := make([]rune, 0)
    for _, b := range brackets {
        if b == '(' {
            stack = append(stack, b)
        }else if b == ')' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}



