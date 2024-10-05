    var stack []rune

    for _, s := range lst {
        for _, r := range s {
            if r == '(' {
                stack = append(stack, r)
            } else {
                if len(stack) == 0 {
                    return "No"
                }
                stack = stack[:len(stack) - 1]
            }
        }
    }
    if len(stack) == 0 {
        return "Yes"
    } else {
        return "No"
    }
}



