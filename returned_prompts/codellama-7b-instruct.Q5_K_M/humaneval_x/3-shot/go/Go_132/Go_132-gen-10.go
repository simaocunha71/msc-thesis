    var stack = make([]int, 0)

    for _, c := range s {
        if c == '[' {
            stack = append(stack, 1)
        }else if c == ']' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    if len(stack) != 0 {
        return false
    }

    return true
}



