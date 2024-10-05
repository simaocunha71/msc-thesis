    balance := 0
    for _, c := range s {
        if c == '(' {
            balance++
        } else {
            balance--
        }
        if balance < 0 {
            return "No"
        }
    }
    if balance != 0 {
        return "No"
    }
    return "Yes"
}


