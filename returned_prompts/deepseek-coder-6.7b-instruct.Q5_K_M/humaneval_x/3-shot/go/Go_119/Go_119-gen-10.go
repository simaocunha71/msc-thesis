    var open_count, close_count int
    for _, str := range lst {
        for _, ch := range str {
            if ch == '(' {
                open_count++
            } else if ch == ')' {
                if open_count > 0 {
                    open_count--
                } else {
                    return "No"
                }
            }
        }
    }
    if open_count == 0 {
        return "Yes"
    }
    return "No"
}



