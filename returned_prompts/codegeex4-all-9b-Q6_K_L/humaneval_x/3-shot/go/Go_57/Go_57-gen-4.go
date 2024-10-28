    if len(l) == 1 {
        return true
    }
    increasing := l[0] <= l[1]
    for i := 1; i < len(l)-1; i++ {
        if (increasing && l[i] >= l[i+1]) || (!increasing && l[i] <= l[i+1]) {
            return false
        }
    }
    return true
}

