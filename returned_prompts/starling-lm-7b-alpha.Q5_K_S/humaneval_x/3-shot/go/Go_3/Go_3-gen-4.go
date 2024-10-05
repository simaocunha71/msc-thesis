    balance := 0
    for _, operation := range operations {
        if balance + operation < 0 {
            return true
        }
        balance += operation
    }
    return false
}



