    depth := 0
    for _, s := range lst {
        for _, r := range s {
            if r == '(' {
                depth += 1
            }else if r == ')' {
                depth -= 1
                if depth < 0 {
                    return "No"
                }
            }
        }
    }
    if depth == 0 {
        return "Yes"
    } else {
        return "No"
    }
}



