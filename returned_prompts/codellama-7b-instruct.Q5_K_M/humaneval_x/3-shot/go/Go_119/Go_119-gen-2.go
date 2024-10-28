    var stack []rune
    for _, s := range lst {
        for _, c := range s {
            switch c {
            case '(':
                stack = append(stack, c)
            case ')':
                if len(stack) == 0 {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) == 0 {
        return "Yes"
    } else {
        return "No"
    }
}



