    current_balance := 0
    for i := 0; i < len(operations); i++ {
        current_balance += operations[i]
        if current_balance < 0 {
            return true
        }
    }
    return false
}



