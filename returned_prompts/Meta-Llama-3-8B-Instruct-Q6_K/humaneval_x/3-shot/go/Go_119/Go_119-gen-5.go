    open_count := 0
    close_count := 0

    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                open_count += 1
            } else if c == ')' {
                close_count += 1
                if open_count == 0 {
                    return "No"
                }
                open_count -= 1
            }
        }
    }
    if open_count != 0 {
        return "No"
    }
    return "Yes"
}