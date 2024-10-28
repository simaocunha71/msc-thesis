    if len(l) <= 1 {
        return true
    }

    for i := 1; i < len(l); i++ {
        if l[i] != l[i-1] && l[i] != l[i-1] + 1 {
            return false
        }
    }
    return true
}



