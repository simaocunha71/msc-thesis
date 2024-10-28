    balance := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                balance += 1
            } else if c== ')' {
                balance -= 1
            }
            if balance < 0 {
                return "No"
            }
        }
    }
    if balance != 0 {
        return "No"
    }
    return "Yes"
}



