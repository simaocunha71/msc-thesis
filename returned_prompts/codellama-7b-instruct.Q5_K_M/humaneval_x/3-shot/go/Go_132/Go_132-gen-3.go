    var stack []rune
    for _, r := range s {
        if r == '[' {
            stack = append(stack, r)
        } else if r == ']' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}



