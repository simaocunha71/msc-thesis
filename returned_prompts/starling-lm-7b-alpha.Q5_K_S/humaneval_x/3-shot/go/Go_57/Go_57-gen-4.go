    for i := 0; i < len(l) - 1; i++ {
        if l[i] < l[i + 1] {
            return false
        }
    }
    return true
}



