    stack := []rune{}
    for _, c := range brackets {
        if string(c) == "(" {
            stack = append(stack, c)
        }else if string(c) == ")" {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}