    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[i-1]+1 {
            return false
        }
    }
    return true
}



