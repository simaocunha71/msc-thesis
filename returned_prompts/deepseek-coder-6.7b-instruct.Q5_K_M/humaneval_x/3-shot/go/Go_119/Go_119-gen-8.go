    var s1 string = lst[0] + lst[1]
    var stack []rune

    for _, c := range s1 {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            if len(stack) == 0 {
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



