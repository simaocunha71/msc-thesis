    if len(l) < 2 {
        return true
    }

    increase := l[1] > l[0]
    for i := 2; i < len(l); i++ {
        if (l[i] > l[i-1]) != increase {
            return false
        }
    }
    return true
}



