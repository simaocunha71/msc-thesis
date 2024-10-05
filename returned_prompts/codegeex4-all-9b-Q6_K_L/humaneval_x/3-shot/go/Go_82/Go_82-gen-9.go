    if len(s) < 2 {
        return false
    }
    for i := 2; i < len(s); i++ {
        if len(s)%i == 0 {
            return false
        }
    }
    return true
}

