    var depth int = 0
    for _, c := range lst[0] {
        if c == '(' {
            depth += 1
        } else {
            depth -= 1
        }
    }
    if depth == 0 {
        return "Yes"
    }
    depth = 0
    for _, c := range lst[1] {
        if c == '(' {
            depth += 1
        } else {
            depth -= 1
        }
    }
    if depth == 0 {
        return "Yes"
    }
    return "No"
}



