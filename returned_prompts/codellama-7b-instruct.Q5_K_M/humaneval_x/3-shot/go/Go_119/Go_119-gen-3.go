    var stack []rune
    for _, str := range lst {
        for _, c := range str {
            if c == '(' {
                stack = append(stack, c)
            } else {
                if len(stack) == 0 {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) == 0 {
        return "Yes"
    }
    return "No"
}



