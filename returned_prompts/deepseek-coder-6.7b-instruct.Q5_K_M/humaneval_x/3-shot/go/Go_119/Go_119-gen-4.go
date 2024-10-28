    s1 := lst[0] + lst[1]
    stack := []rune{}
    for _, c := range s1 {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return "No"
            }
            stack = stack[:len(stack)-1]
        }
    }
    if len(stack) == 0 {
        return "Yes"
    }
    return "No"
}



