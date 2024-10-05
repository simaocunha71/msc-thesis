    depth := 0
    for _,s := range lst {
        for _,c := range s {
            if c == '(' {
                depth++
            }else if c==')' {
                depth--
            }
            if depth < 0 {
                return "No"
            }
        }
        if depth != 0 {
            return "No"
        }
    }
    return "Yes"
}



