    var balance int = 0
    for i := 0; i < len(operations); i++ {
        balance += operations[i]
        if balance < 0 {
            return true
        }
    }
    return false
}



