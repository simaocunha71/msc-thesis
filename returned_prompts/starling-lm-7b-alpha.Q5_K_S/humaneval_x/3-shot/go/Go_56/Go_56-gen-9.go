    stack := make([]rune, 0)
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c)
        }else if c == '>' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            }else {
                return false
            }
        }
    }
    return len(stack) == 0
}



