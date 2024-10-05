    if s == "" {
        return true
    }
    for i := 2; i < len(s); i++ {
        if len(s)%i == 0 {
            return false
        }
    }
    return true
}

