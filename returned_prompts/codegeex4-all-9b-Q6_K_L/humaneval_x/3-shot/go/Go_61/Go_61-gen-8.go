    open := 0
    for _, c := range brackets {
        if c == '(' {
            open += 1
        } else if c == ')' {
            open -= 1
        }
        if open < 0 {
            return false
        }
    }
    return open == 0
}



