    stack := make([]rune, 0)
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                stack = append(stack, c)
            } else if c == ')' {
                if len(stack) == 0 {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    return len(stack) == 0 ? "Yes" : "No"
}



