    if len(lst) == 0 {
        return true
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] <= lst[i-1] {
            return false
        }
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] == lst[i-1] {
            return false
        }
    }
    return true
}