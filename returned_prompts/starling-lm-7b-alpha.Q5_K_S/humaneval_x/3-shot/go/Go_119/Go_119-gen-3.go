    depth := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                depth += 1
            } else if c == ')' {
                depth -= 1
            }
            if depth < 0 {
                return "No"
            }
        }
    }
    if depth != 0 {
        return "No"
    }
    return "Yes"
}



