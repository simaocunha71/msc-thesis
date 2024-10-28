    var stack []rune

    for _, b := range brackets {
        if b == '>' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack) - 1]
        } else {
            stack = append(stack, b)
        }
    }

    return len(stack) == 0
}



