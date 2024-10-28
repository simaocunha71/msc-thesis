    balance := 0
    for _, v := range operations {
        balance += v
        if balance < 0 {
            return true
        }
    }
    return false
}



