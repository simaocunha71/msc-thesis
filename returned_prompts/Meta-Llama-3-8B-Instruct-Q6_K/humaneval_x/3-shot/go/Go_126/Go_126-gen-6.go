    for i := 1; i < len(lst); i++ {
        if lst[i] < lst[i-1] {
            return false
        }
        if lst[i] == lst[i-1] {
            for j := i+1; j < len(lst); j++ {
                if lst[j] < lst[i] {
                    return false
                }
            }
        }
    }
    return true
}