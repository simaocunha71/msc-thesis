    if len(l) < 2 {
        return true
    }
    for i := 0; i < len(l) - 1; i++ {
        if l[i] > l[i + 1] {
            return false
        }
    }
    return true
}



