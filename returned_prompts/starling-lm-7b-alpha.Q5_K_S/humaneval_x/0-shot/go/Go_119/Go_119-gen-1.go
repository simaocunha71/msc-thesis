
    stack := []rune{}
    for _, v := range lst[0] {
        if v == '(' {
            stack = append(stack, v)
        } else {
            if len(stack) == 0 {
                return "No"
            } else {
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) == 0 {
        for _, v := range lst[1] {
            if v == '(' {
                stack = append(stack, v)
            } else {
                if len(stack) == 0 {
                    return "No"
                } else {
                    stack = stack[:len(stack)-1]
                }
            }
        }
        if len(stack) == 0 {
            return "Yes"
        } else {
            return "No"
        }
    } else {
        return "No"
    }
    return "No"
}

















































































































































































































































































