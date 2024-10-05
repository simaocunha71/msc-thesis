    if len(l) < 2 {
        return true
    }
    isIncreasing := l[0] < l[1]
    for i := 1; i < len(l); i++ {
        if isIncreasing {
            if l[i] < l[i-1] {
                return false
            }
        } else {
            if l[i] > l[i-1] {
                return false
            }
        }
    }
    return true
}

