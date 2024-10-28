    open := 0
    close := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                open++
            } else if c == ')' {
                close++
            }
        }
    }
    if open == close {
        return "Yes"
    }
    return "No"
}