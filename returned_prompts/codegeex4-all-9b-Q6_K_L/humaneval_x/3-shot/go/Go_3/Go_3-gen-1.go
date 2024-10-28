    var balance int = 0
    for _, op := range operations {
        balance += op
        if balance < 0 {
            return true
        }
    }
    return false
}

