    if len(lst) == 1 {
        return true
    }

    for i := 0; i < len(lst) - 1; i++ {
        if lst[i] == lst[i+1] {
            return false
        }
        if lst[i] > lst[i+1] {
            return false
        }
    }
    return true
}



