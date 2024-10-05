    var current_balance int
    for _, operation := range operations {
        current_balance += operation
        if current_balance < 0 {
            return true
        }
    }
    return false
}



