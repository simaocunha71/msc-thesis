    if len(l) <= 2 {
        return true
    }

    increasing := l[0] < l[1]
    for i := 1; i < len(l); i++ {
        if increasing && l[i] < l[i-1] {
            return false
        } else if !increasing && l[i] > l[i-1] {
            return false
        }
    }
    return true
}



