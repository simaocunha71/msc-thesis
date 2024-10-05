    s1, s2 := lst[0], lst[1]
    balance := 0
    for _, c := range s1+s2 {
        if c == '(' {
            balance++
        } else {
            balance--
            if balance < 0 {
                return "No"
            }
        }
    }
    return "Yes" if balance == 0 else "No"
}



