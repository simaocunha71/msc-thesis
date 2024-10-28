    if len(l) <= 1 {
        return true
    }
    ascending := l[0] <= l[1]
    for i := 1; i < len(l); i++ {
        if (l[i-1] < l[i]) != ascending {
            return false
        }
    }
    return true
}



