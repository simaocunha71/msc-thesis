    balance := 0
    for _, operation := range operations {
        balance += operation
        if balance < 0 {
            return true
        }
    }
    return false
}
}}



