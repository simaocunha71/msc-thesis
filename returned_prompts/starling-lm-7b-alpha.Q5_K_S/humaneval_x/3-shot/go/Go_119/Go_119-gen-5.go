    depth := 0
    for _, s := range lst {
        for _, r := range s {
            if r == '(' {
                depth += 1
            } else if r == ')' {
                depth -= 1
            }
        }
        if depth < 0 {
            return "No"
        }
    }
    return (depth == 0) ? "Yes" : "No"
}



