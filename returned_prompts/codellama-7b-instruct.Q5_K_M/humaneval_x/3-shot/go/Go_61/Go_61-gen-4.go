    stack := make([]rune, 0)

    for _, bracket := range brackets {
        if bracket == '(' {
            stack = append(stack, bracket)
        }else if bracket == ')' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}



