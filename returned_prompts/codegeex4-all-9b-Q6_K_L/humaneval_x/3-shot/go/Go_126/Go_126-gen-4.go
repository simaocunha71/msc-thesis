    for i := 0; i < len(lst); i++ {
        for j := i + 1; j < len(lst); j++ {
            if lst[i] > lst[j] {
                return false
            }
        }
    }
    return true
}



