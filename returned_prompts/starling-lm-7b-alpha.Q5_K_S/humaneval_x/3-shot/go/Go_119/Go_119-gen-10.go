    depth := 0
    for _, s := range lst {
        for _, r := range s {
            if r == '(' {
                depth++
            }else if r == ')' {
                depth--
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



