    open_count := 0
    close_count := 0

    for _, str := range lst {
        for _, c := range str {
            if c == '(' {
                open_count += 1
            } else if c == ')' {
                close_count += 1
            }
        }
        if open_count > close_count {
            return "No"
        }
        open_count = 0
        close_count = 0
    }
    if close_count > open_count {
        return "No"
    }
    return "Yes"
}