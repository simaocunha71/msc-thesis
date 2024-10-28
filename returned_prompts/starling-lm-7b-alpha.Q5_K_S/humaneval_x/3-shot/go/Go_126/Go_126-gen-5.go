    for i := 1; i < len(lst); i++ {
        if lst[i-1] > lst[i] {
            return false
        }
    }
    return true
}



