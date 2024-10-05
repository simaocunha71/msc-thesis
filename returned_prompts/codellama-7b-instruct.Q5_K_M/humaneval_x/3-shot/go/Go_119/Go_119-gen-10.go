    var stack = make([]string, 0)

    for _, s := range lst {
        if s == "(" {
            stack = append(stack, s)
        } else {
            if len(stack) == 0 {
                return "No"
            }
            stack = stack[:len(stack)-1]
        }
    }

    if len(stack) == 0 {
        return "Yes"
    } else {
        return "No"
    }
}



