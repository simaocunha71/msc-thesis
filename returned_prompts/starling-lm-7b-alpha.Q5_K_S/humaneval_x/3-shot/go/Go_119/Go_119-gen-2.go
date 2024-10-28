    left_depth := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                left_depth++
            }else if c == ')' {
                left_depth--
            }
        }
        if left_depth < 0 {
            return "No"
        }
    }
    return "Yes"
}



