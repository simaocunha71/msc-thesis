    for i := 1; i < len(l); i++ {
        if l[i-1] < l[i] {
            return false
        }
    }
    return true
}



