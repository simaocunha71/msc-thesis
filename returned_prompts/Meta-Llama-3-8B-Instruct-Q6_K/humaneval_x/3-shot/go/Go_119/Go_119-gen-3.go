    open_count := 0
    close_count := 0

    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                open_count += 1
            } else {
                close_count += 1
            }
        }
    }

    if open_count == close_count {
        return "Yes"
    } else {
        return "No"
    }
}