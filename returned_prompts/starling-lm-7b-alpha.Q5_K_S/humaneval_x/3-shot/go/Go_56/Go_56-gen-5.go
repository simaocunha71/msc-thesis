    stack := make([]rune, 0)

    for _, c := range brackets {
        switch c {
        case '<':
            stack = append(stack, c)
        case '>':
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}



