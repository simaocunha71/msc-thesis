    for i := 0; i < len(lst) - 1; i++ {
        if lst[i + 1] < lst[i] {
            return false
        }
    }
    return true
}



