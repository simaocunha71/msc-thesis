    var open_count = 0
    for _, c := range lst[0] {
        if c == '(' {
            open_count += 1
        } else if c == ')' {
            open_count -= 1
        }
    }
    if open_count != 0 {
        return "No"
    }
    var open_count = 0
    for _, c := range lst[1] {
        if c == '(' {
            open_count += 1
        } else if c == ')' {
            open_count -= 1
        }
    }
    if open_count != 0 {
        return "No"
    }
    return "Yes"
}



