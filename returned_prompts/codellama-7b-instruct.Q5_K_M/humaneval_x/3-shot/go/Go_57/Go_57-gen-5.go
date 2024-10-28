    if len(l) <= 2 {
        return true
    }

    for i := 1; i < len(l); i++ {
        if l[i] < l[i - 1] {
            return false
        }
    }
    return true
}



